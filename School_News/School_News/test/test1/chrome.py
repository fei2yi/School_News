from selenium import webdriver
from scrapy.http import HtmlResponse


def get_url(url):
    b = webdriver.Chrome()
    b.get(url)
    return HtmlResponse(body=b.page_source.encode('utf8'), encoding='utf8', url=b.current_url)

a = get_url('http://www.hnjxw.gov.cn/xxgk_71033/jgzn/jgzn/')
print(a.text)
