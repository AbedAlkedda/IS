import pdb # noqa
import logging

from Crawler import Crawler
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from spyne import Application, rpc, ServiceBase, Integer, Unicode, Iterable, ComplexModel


class HtwkInfo(ComplexModel):
    __namespace__ = 'HtwkInfo'
    semester_duration = Unicode()
    precourses = Unicode()
    introductory_events = Unicode()
    lecture_period = Unicode()
    exam_period = Unicode()
    lecture_break = Unicode()


class MovieData(ComplexModel):
    __namespace__ = 'MovieData'

    title = Unicode()
    year = Unicode()
    rating = Unicode()
    link = Unicode()
    thumbnail = Unicode()


# SOAP Server
class CrawlerServer(ServiceBase):
    crawler = Crawler().run(format='json')

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

    @rpc(Integer, _returns=Iterable(MovieData))
    def movies_data(ctx, elements):
        res = []
        for m in crawler.movie_data[:elements]:
            movie_data = MovieData(title=m['title'],
                                   year=m['year'],
                                   rating=m['rating'],
                                   link=m['link'],
                                   thumbnail=m['thumbnail'])
            res.append(movie_data)

        return res

    @rpc(_returns=HtwkInfo)
    def htwk_info(ctx):
        crawler.htwk_info()
        return HtwkInfo(
            semester_duration=crawler.res['Semesterdauer'],
            precourses=crawler.res['Vorkurse'],
            introductory_events=crawler.res['Einfhrungsveranstaltungen'],
            lecture_period=crawler.res['Vorlesungszeitraum'],
            exam_period=crawler.res['Prfungsperioden'],
            lecture_break=crawler.res['Vorlesungsunterbrechungen']
        )


application = Application([CrawlerServer], tns='crawler.example',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

if __name__ == '__main__':
    crawler = Crawler()
    crawler.run()

    server = make_server('', 8000, WsgiApplication(application))
    logging.basicConfig(level=logging.DEBUG)
    logging.info('starting server')
    server.serve_forever()
