class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.used_urls = set()

    def add_new_urls(self, urls):
        self.urls = set()
        self.urls = urls
        if self.urls is None or len(self.urls) == 0:
            return
        for url in self.urls:
            if url not in self.new_urls and url not in self.used_urls:
                self.new_urls.add(url)

    def has_new_url(self):
        return len(self.new_urls) > 0

    def get_new_url(self):
        temp_url = self.new_urls.pop()
        self.used_urls.add(temp_url)
        return temp_url