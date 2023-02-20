# ToDo: seperate the big method into smaller once
# DRY the code
# Check for wiki page, important

import pdb # noqa
from pprint import pprint # noqa

import requests
from bs4 import BeautifulSoup


class Crawler:
    def __init__(self):
        self.movie_data = []
        self.titles = []
        self.years = []
        self.ratings = []
        self.links = []
        self.thumbnails = []

    def crawl(self):
        response = requests.get('https://www.imdb.com/chart/top/')
        soup = BeautifulSoup(response.text, 'html.parser')

        movie_table = soup.find('tbody', {'class': 'lister-list'})
        movies = movie_table.find_all('tr')

        for movie in movies:
            title_column = movie.find('td', {'class': 'titleColumn'})
            rating_column = movie.find('td', {'class': 'ratingColumn'})

            title = title_column.a.text
            self.titles.append(title)

            year = title_column.span.text.strip('()')
            self.years.append(year)

            rating = rating_column.strong.text
            self.ratings.append(rating)

            link = title_column.a['href']
            self.links.append(link)

            thumbnail = movie.find('td', {'class': 'posterColumn'}).a.img['src']
            self.thumbnails.append(thumbnail)

            self.movie_data.append({
                'title': title,
                'year': year,
                'rating': rating,
                'link': 'https://www.imdb.com' + link,
                'thumbnail': thumbnail
            })

    def movies(self, format='json'):
        if not self.movie_data:
            self.crawl()

        if format == 'json':
            return self.movie_data
