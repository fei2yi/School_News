# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request
import pymysql
from School_News.items import Article
from School_News.lib.loader import ArticleLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ArticlezlSpider(Spider):
    name = 'articlezl'
    allowed_domains = []
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='yyaiyi',
                           db='school_news',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    # cursor.execute("SELECT * FROM eachlistlinkitem a INNER "
    #                "JOIN eachpageslinkitem b ON a.listUrl = b.parent WHERE pageSum='0'")
    #
    # a = cursor.fetchall()

    cursor.execute("SELECT listUrl FROM eachlistlinkitem")

    all_list = cursor.fetchall()

    list_l = []
    # for i in all_list:
    #     cursor.execute("SELECT pageUrl, xpath FROM eachlistlinkitem a INNER "
    #                "JOIN eachpageslinkitem b ON a.listUrl = b.parent WHERE(parent='{}' and pageSum='0')".format(i.get('listUrl')))
    #     list_pages = cursor.fetchall()
    #     list_pages = sorted(list_pages, key=lambda d: d, reverse=True)
    #     list_l.append(list_pages)
    print(list_l)
    # start_urls = [[i.get('pageUrl'), i.get('xpath')] for i in a]
    start_urls = [i for i in list_l]

    def start_requests(self):
        for i in self.start_urls:
            request = Request(i.get('pageUrl'), meta={'xpath': i.get('xpath')})
            # request.meta['PhantomJS'] = True
            yield request

    def parse(self, response):
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
