from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def index():
    url = 'https://www.imdb.com/chart/top/'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    movie_data = []

    for movie in soup.find('tbody', {'class': 'lister-list'}).find_all('tr'):
        title_column = movie.find('td', {'class': 'titleColumn'})
        rating_column = movie.find('td', {'class': 'ratingColumn'})

        title = title_column.a.text
        year = title_column.span.text.strip('()')
        rating = rating_column.strong.text

        movie_data.append({'title': title, 'year': year, 'rating': rating})

    return render_template('index.html', movies=movie_data)


if __name__ == '__main__':
    app.run()
