from bs4 import BeautifulSoup
import requests


class Crawler:
    def __init__(self):
        self.movie_data = []

    def crawl(self):
        response = requests.get('https://www.imdb.com/chart/top/')
        soup = BeautifulSoup(response.text, 'html.parser')

        movie_table = soup.find('tbody', {'class': 'lister-list'})
        movies = movie_table.find_all('tr')

        for movie in movies:
            title_column = movie.find('td', {'class': 'titleColumn'})
            rating_column = movie.find('td', {'class': 'ratingColumn'})

            title = title_column.a.text
            year = title_column.span.text.strip('()')
            rating = rating_column.strong.text
            args = {'title': title, 'year': year, 'rating': rating}
            self.movie_data.append(args)

    def get_movies(self):
        if not self.movie_data:
            self.crawl()
        return self.movie_data
