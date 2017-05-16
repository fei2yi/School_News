from scrapy.http import Request
from School_News.items import EachListLinkItem
from School_News.lib.loader import EachListLinkLoader
from scrapy import Spider
from School_News.lib.transporturl import transport
import pymysql


class ArticleSpider(Spider):
    name = 'article'
    allowed_domains = []
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='yyaiyi',
                           db='school_news',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM eachlistlinkitem a")

    a = cursor.fetchall()
    start_urls = [[i.get('listUrl'), i.get('list'), i.get('parent')] for i in a]

    def start_requests(self):
        for urll in self.start_urls:
            url = urll[0]
            request = Request(url, meta={'listUrl': url, 'list': urll[1], 'parent': urll[2]})
            # request.meta['PhantomJS'] = True
            yield request

    def parse(self, response):
        pass