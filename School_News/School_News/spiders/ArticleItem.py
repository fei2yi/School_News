# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request
import pymysql
from School_News.items import EachArticleLinkItem
from School_News.lib.loader import EachArticleLinkLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from School_News.lib.transporturl import transport


class ArticleItemSpider(Spider):
    name = 'articleitem'
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
                   "JOIN eachpageslinkitem2 b ON a.listUrl = b.parent WHERE pageSum='0'")

    a = cursor.fetchall()
    start_urls = [[i.get('pageUrl'), i.get('xpath')] for i in a]

    def start_requests(self):
        for urll in self.start_urls:
            request = Request(urll[0], meta={'listUrl': urll[0], 'xpath': urll[1]})
            # request.meta['PhantomJS'] = True
            yield request

    def parse(self, response):
        yield from self.AItem(response)

    def AItem(self, response):
        xpath = response.meta.get('xpath')
        xpath = xpath.spilt('#')
        ul = response.xpath(xpath[0])[xpath[1]]
        li = ul.xpath(xpath[2])
        for index, li in enumerate(li):
            cci = EachArticleLinkLoader(item=EachArticleLinkItem(), selector=li, response=response)
            cci.add_xpath('title', './/a/text() | .//a/@title')
            cci.add_xpath('textUrl', './/a/@href')
            cci.add_xpath('publishTime', './/span/text()')
            cci.add_value('parent', response.url)
            cciitme = cci.load_item()
            yield cciitme
