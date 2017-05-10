# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from School_News.lib.transporturl import transport


class PageCollectSpider(CrawlSpider):
    name = 'PageCollect'
    allowed_domains = []
    # start_urls = [i for i in transport('WebsiteCollect.json', 'link')]
    start_urls = ['']

    rules = (
        Rule(LinkExtractor(allow=('(.*)xwzh_(.*)',)), callback='parse_item', follow=True),
    )

    def parse_start_url(self, response):
            request = Request(response.url)
            # request.meta['PhantomJS'] = True
            yield request

    def parse_item(self, response):
        self.logger.info('Hi, %s', response.url)
        item = scrapy.Item()
        item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
        item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
        print(item['id'], item['name'])
        return item




        # name = 'Seg'
        # allowed_domains = ['pku.edu.cn']
        # start_urls = [
        #     'http://pkunews.pku.edu.cn/xwzh/xwzh.htm',  #
        # ]
        #
        # rules = (
        #     Rule(SgmlLinkExtractor(allow=('^http://pkunews\.pku\.edu\.cn/xwzh$', ))),
        #     Rule(SgmlLinkExtractor(allow=('http://pkunews.pku.edu.cn/xwzh', )), callback='parse_item'),
        # )
        #
        # def parse_item(self, response):
        #     print('1')

# class LoginSpider(scrapy.Spider):
#     name = 'baidu.com'
#     start_urls = ['https://www.baidu.com/link?url=HIpCLuemVGTQStM0RCHi7tX68MnkUkWAC9-MdR6q8XGkFz_VAGzlqfuZ2EkxHCP9&wd=&eqid=ab16dcf00005d09b00000003590d735c']
#
#     def parse(self, response):
#         a=response.xpath('substring-before(substring-after(//script/text(),\'replace("\'), \'")}\')')
#         print(a,response.text)
