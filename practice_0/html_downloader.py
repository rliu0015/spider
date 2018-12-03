from urllib import request
class HtmlDownloader(object):
    def downloader(self, url):
        if url is None:
            return
        response = request.urlopen(url)
        if response.getcode() != 200:
            return
        return response.read()