from scrapy.http import HtmlResponse
from selenium import webdriver


def get(url, wait=0, browser='chrome'):
    br = webdriver.Chrome() if browser == 'chrome' else webdriver.PhantomJS()
    br.implicitly_wait(wait)
    br.get(url)
    source = br.page_source
    br.quit()
    return HtmlResponse(body=source, encoding='utf8', url=url)

def gen(txt, url='[null]'):
    return HtmlResponse(body=txt.encode('utf8'), encoding='utf8', url=url)
