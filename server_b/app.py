# # ToDo: SOAP flask out

from spyne import Application, rpc, ServiceBase, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


class CrawlerServer(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add_numbers(ctx, a, b):
        return a + b


application = Application([CrawlerServer], tns='crawler.example',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('localhost', 5000, WsgiApplication(application))
    server.serve_forever()
