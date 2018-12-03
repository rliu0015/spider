import time
class Output(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        file_name = "out_" + time.strftime("%Y_%m_%d_%H-%M-%S") + ".html"
        with open(file_name, 'w+' , encoding='utf-8') as outf:
            outf.write("<html>")
            outf.write(r'<head>'
                        r'<link rel="stylesheet" '
                        r'href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" '
                        r'integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" '
                        r'crossorigin="anonymous"></head>')
            outf.write("<body>")
            outf.write(r'<table class="table table-bordered table-hover">')

            item_css = ['active', 'success', 'warning', 'info']
            for data in self.datas:
                index = self.datas.index(data) % len(item_css)
                outf.write(r'<tr class="'+item_css[index]+r'">')
                outf.write('<td>%s</td>' % data["url"])
                outf.write('<td>%s</td>' % data["title"])
                outf.write('<td>%s</td>' % data["summary"])
                outf.write("</tr>")
            outf.write("</table>")
            outf.write("</body>")
            outf.write("</html>")