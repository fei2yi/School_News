from scrapy.http import Request
from School_News.items import Page, Article
from School_News.lib.loader import PageLoader, ArticleLoader
from scrapy import Spider
import pymysql


class PageSpider(Spider):
    name = 'page'
    allowed_domains = []
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='yyaiyi',
                           db='school_news',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM eachlistlinkitem a INNER "
                   "JOIN eachpageslinkitem b ON a.listUrl = b.parent")

    a = cursor.fetchall()
    start_urls = [[i.get('pageUrl'), i.get('xpath')] for i in a]

    def start_requests(self):
        for urll in self.start_urls:
            url = urll[0]
            request = Request(url, meta={'listUrl': url, 'list': urll[1], 'xpath': urll[2], 'parent': url})
            # request.meta['PhantomJS'] = True
            yield request

    def parse(self, response):
        yield from self.nextpage(response)

    num = 0

    def nextpage(self, response):
        pass

    def yield_item(self, url, pageNum, pageSum, parent):
        epll = PageLoader(item=Page())
        epll.add_value('pageUrl', url)
        epll.add_value('pageNum', pageNum)
        epll.add_value('pageSum', pageSum)
        epll.add_value('parent', parent)
        epllitme = epll.load_item()
        yield epllitme

    def parse_item(self, response):
        xpath = response.meta.get('xpath')
        xp = xpath.split('#')
        ul = response.xpath(xp[0])[int(xp[1])]
        li = ul.xpath(xp[2])
        for index, li in enumerate(li):
            cci = ArticleLoader(item=Article(), selector=li, response=response)
            cci.add_xpath('title', './/a/text() | .//a/@title')
            cci.add_xpath('textUrl', './/a/@href')
            cci.add_xpath('publishTime', './/span/text()')
            cci.add_value('parent', response.url)
            cciitme = cci.load_item()
            if not cciitme.get('publishTime'):
                cci.add_value('publishTime', 'null')
            if not cciitme.get('title'):
                cci.add_value('title', 'null')
            if not cciitme.get('textUrl'):
                cci.add_value('textUrl', 'null')
            cciitme = cci.load_item()
            print('---')
            print(cciitme.get('title'), cciitme.get('textUrl'), xpath)
            yield cciitme
