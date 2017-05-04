# -*- coding: utf-8 -*-
# 贵州省能源局

from scrapy.http import Request
from scrapy.loader import ItemLoader
from scrapy import Spider


class GzcoalSpider(Spider):
    name = 'gzcoal_gov_cn.GzcoalSpider'
    allowed_domains = ['gzcoal.gov.cn']
    start_urls = [
        'http://www.gzcoal.gov.cn/list.jsp?itemId=6&cItemId=104&page=1',  # 国务院文件专栏
        'http://www.gzcoal.gov.cn/list.jsp?itemId=6&cItemId=105&page=1',  # 省政府文件专栏
    ]

    def parse(self, response):
        group = response.xpath('//div[@class="news_tit"]/text()').extract_first()
        for index, li in enumerate(response.xpath('//div[@class="articleList"]//li')):
            l = ItemLoader(selector=li, response=response)
            l.add_value('group', group)
            l.add_xpath('url', './/a/@href')
            l.add_xpath('title', './/a/text()')
            l.add_xpath('publish_time', 'span[@class="time"]/text()')
            item = l.load_item()

            yield Request(item['url'], callback=self.parse_item, meta={'index': index, 'item': item})
        next_page = self.parse_next_page()
        if next_page and next_page.get_attribute('disabled') != 'true':
            yield self.action(action=next_page.click, callback=self.parse)

    def parse_next_page(self):
        ls = [input for input in self.browser.find_elements_by_xpath('//*[@id="page_1"]/input[4]')
              if input.get_attribute('value') == '下一页']
        return ls[0] if ls else None

    def parse_item(self, response):
        l = ItemLoader(response.meta['item'], response=response)
        l.add_xpath('source', 'substring-before(substring-after(//div[@class="wh"]/text(), "来源："), "日期：")')
        l.add_xpath('content', '//div[@class="zw"]')
        l.add_xpath('file_urls', '//div[@class="zw"]//a')
        yield l.load_item()

