
from scrapy.http import Request
from School_News.items import Content
from School_News.lib.loader import ContentLoader

from scrapy import Spider
import pymysql


class weiboSpider(Spider):
    name = 'weibo'
    allowed_domains = []
    xpaths = []
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='yyaiyi',
                           db='school_news',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    cursor.execute("SELECT url,child FROM college")
    url_and_child = cursor.fetchall()

    start_urls = ['http://weibo.com/1713926427/F4bNka5rg?filter=hot&root_comment_id=0&type=comment#_rnd1496559767302',
                  'http://weibo.com/u/5746839483?from=myfollow_all']

    def start_requests(self):
        for url_and_child in self.start_urls:
            request = Request(url_and_child)
            request.meta['PhantomJS'] = True
            yield request

    def parse(self, response):
        authors_and_content=response.xpath('//div[@class="WB_text"]')
        for i in authors_and_content:
            eltl = ContentLoader(item=Content(), selector=i, response=response)
            eltl.add_xpath('content', 'a[1]/text()')
            eltl.add_xpath('author', './text()[last]')
            eltlitme = eltl.load_item()
            yield eltlitme

