import pdb # noqa
import logging

from Crawler import Crawler
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from spyne import Application, rpc, ServiceBase, Integer, Unicode, Iterable


# SOAP Server
class CrawlerServer(ServiceBase):
    crawler = Crawler().movies(format='json')

    @rpc(Integer, Integer, _returns=Integer)
    def add_numbers(ctx, a, b):
        return a + b

    @rpc(Integer, _returns=Iterable(Unicode))
    def titles(ctx, elements):
        return crawler.titles[:elements]

    @rpc(Integer, _returns=Iterable(Unicode))
    def years(ctx, elements):
        return crawler.years[:elements]

    @rpc(Integer, _returns=Iterable(Unicode))
    def ratings(ctx, elements):
        return crawler.ratings[:elements]

    @rpc(Integer, _returns=Iterable(Unicode))
    def links(ctx, elements):
        return crawler.links[:elements]

    @rpc(Integer, _returns=Iterable(Unicode))
    def tubmbnails(ctx, elements):
        return crawler.thumbnails[:elements]


application = Application([CrawlerServer], tns='crawler.example',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

if __name__ == '__main__':
    crawler = Crawler()
    xml_data = crawler.movies()

    server = make_server('localhost', 8000, WsgiApplication(application))
    logging.basicConfig(level=logging.DEBUG)
    logging.info('starting server')
    server.serve_forever()
