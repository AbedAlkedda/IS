# ToDo: seperate the big method into smaller once
# DRY the code
# Check for wiki page, important

import pdb # noqa
import requests
import logging
import re

from pprint import pprint # noqa
from bs4 import BeautifulSoup


class Crawler:
    def __init__(self):
        self.movie_data = []
        self.titles = []
        self.years = []
        self.ratings = []
        self.links = []
        self.thumbnails = []
        self.res = {}
        self.semester_info = ''

    def crawl(self):
        headers = {'Accept-Language': 'en-US,en;q=0.9'}

        response = requests.get('https://www.imdb.com/chart/top/',
                                headers=headers)

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

    def run(self, format='json'):
        if not self.movie_data:
            self.crawl()

        if format == 'json':
            return self.movie_data

    def htwk_info(self, selector=2):
        url = 'https://www.htwk-leipzig.de/studieren/im-studium/akademischer-kalender/'
        response = requests.get(url, verify=True)

        # send a SSL request, otherwise the HTWK wont resposed
        soup = BeautifulSoup(response.content, 'html.parser')

        # find headers and select one
        header_holder = []
        for item in soup.find_all('h2'):
            if 'Wintersemester' in item.text or 'Sommersemester' in item.text:
                header_holder.append(item.text.replace('\t', '').replace('\n', ''))

        self.semester_info = header_holder[selector]

        # Find the table with the class "contenttable"
        contenttable = soup.find_all('table', {'class': 'contenttable'})[selector]

        if contenttable is not None:
            # Find all the table rows (tr elements) within that table
            rows = contenttable.find_all('tr')
            # Print out the contents of each row
            for row in rows:
                ele_in_row = row.find_all('td')

                # Just a label without dates
                if (len(ele_in_row) == 1):
                    ele = ele_in_row[0].text.replace('\t', '')
                    ele = re.sub(r'[^\x00-\x7F]+', '', ele)

                    self.res[ele] = ''

                # label with dates
                if (len(ele_in_row) > 1):
                    category = ele_in_row[0].text.replace('\t', '')
                    category = re.sub(r'[^\x00-\x7F]+', '', category)
                    dates = ele_in_row[1].text.replace('\t', '')
                    dates = re.sub(r'[^\x00-\x7F]+', '', dates)

                    self.res[category] = dates
        else:
            logging.warn("Could not find 'contenttable' on the page.")
