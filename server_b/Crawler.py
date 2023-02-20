from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET


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
            # ToDo: Check for wiki page
            year = title_column.span.text.strip('()')
            rating = rating_column.strong.text
            link = title_column.a['href']
            thumbnail = movie.find('td', {'class': 'posterColumn'}).a.img['src']

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
        elif format == 'xml':
            root = ET.Element('movies')
            for movie in self.movie_data:
                movie_elem = ET.SubElement(root, 'movie')

                title_elem = ET.SubElement(movie_elem, 'title')
                title_elem.text = movie['title']

                year_elem = ET.SubElement(movie_elem, 'year')
                year_elem.text = movie['year']

                rating_elem = ET.SubElement(movie_elem, 'rating')
                rating_elem.text = movie['rating']

                rating_elem = ET.SubElement(movie_elem, 'link')
                rating_elem.text = movie['link']

                rating_elem = ET.SubElement(movie_elem, 'thumbnail')
                rating_elem.text = movie['thumbnail']
            return ET.tostring(root)
