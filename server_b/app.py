from flask import Flask, render_template
from Crawler import Crawler

app = Flask(__name__)
crawler = Crawler()


@app.route('/')
def index():
    movies = crawler.get_movies()
    return render_template('index.html', movies=movies)


if __name__ == '__main__':
    app.run()
