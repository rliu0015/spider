import url_manager
import html_downloader
import html_parser
import html_output

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = html_output.Output()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_urls(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("source %d, %s" % (count, new_url))
                html_content = self.downloader.downloader(new_url)
                new_urls, new_data = self.parser.parser(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_data)
                if count >= 5:
                    break
                count += 1
            except Exception as e:
                print("Exception error:%s" % str(e))
        self.output.output_html()

if __name__ == "__main__":
    url = ["http://baike.baidu.com/item/Android"]
    spider = SpiderMain()
    spider.craw(url)