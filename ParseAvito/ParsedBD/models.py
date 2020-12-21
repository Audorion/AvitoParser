from django.db import models
import requests
from bs4 import BeautifulSoup
import cfscrape
import urllib.parse
import lxml
import datetime
from background_task import background
from django.contrib.auth.models import User


url = ''
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.5',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
}


def get_content():
    session = requests.Session()
    session.headers = HEADERS
    return cfscrape.create_scraper(sess=session)


def parse(URL):
    session = get_content()
    respones = session.get(URL)
    soup = BeautifulSoup(respones.text, "lxml")
    container = soup.find('span', class_='page-title-count-1oJOc').get_text()
    return container.replace(" ", "")


class UserRequest(models.Model):
    region = models.CharField("Регион", max_length=250)
    request_words = models.CharField("Ключевые слова", max_length=250)
    date = models.DateTimeField("Дата запроса", auto_now=True)
    counter = models.IntegerField("Количество результатов", null=True, blank=True, default=0)

    def save(self, *args, **kwargs):
        try:
            url = f'https://www.avito.ru/{self.region}?q={self.request_words}'
            self.counter = int(parse(url))
            super().save(*args, **kwargs)
        except AttributeError:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.request_words

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'
