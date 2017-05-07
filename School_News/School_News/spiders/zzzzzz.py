import scrapy

from scrapy.extensions.feedexport import FeedExporter
# EachArticleLinkLoader
# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor


class SegSpider(CrawlSpider):
    name = 'Seg'
    allowed_domains = ['pku.edu.cn']
    start_urls = [
        'http://pkunews.pku.edu.cn/xwzh/xwzh.htm',  #
    ]

    rules = (
        # 提取匹配 'category.php' (但不匹配 'subsection.php') 的链接并跟进链接(没有callback意味着follow默认为True)

        # 提取匹配 'item.php' 的链接并使用spider的parse_item方法进行分析
        # Rule(LxmlLinkExtractor(allow=('(.*)xwzh_(.*)',)), callback=self.parse_item(), follow=True),
    )

    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        qqq = response.xpath('//a[contains(text(),"下一页")]/@href').extract()
        return print(qqq)



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
