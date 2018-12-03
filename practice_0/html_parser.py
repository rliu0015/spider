from urllib.parse import urljoin
from bs4 import BeautifulSoup
import re
class HtmlParser(object):
    def parser(self, url, data, html_encode = 'utf-8'):
        if url is None or data is None:
            return
        soup = BeautifulSoup(data, 'html.parser', from_encoding=html_encode)
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return new_urls,new_data

    def _get_new_urls(self, url, soup):
        new_urls = set()
        for link in soup.find_all('a'):
            new_urls.add(urljoin(url, link.get('href')))
        return new_urls

    def _get_new_data(self, url, soup):
        new_data = {"url": url}
        new_data["title"] = soup.h1.string
        new_data["summary"] = soup.find("div", class_="lemma-summary").get_text()
        return new_data
