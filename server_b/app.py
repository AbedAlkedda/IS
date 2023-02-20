from flask import Flask, render_template, Response
from Crawler import Crawler

app = Flask(__name__)
crawler = Crawler()


@app.route('/')
def index():
    return render_template('index.html', movies=crawler.movies())


@app.route('/movies.xml')
def movies_xml():
    crawler = Crawler()
    xml_data = crawler.movies(format='xml')
    return Response(xml_data, mimetype='text/xml')


if __name__ == '__main__':
    app.run()
