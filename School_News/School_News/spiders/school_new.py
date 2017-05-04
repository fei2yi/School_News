import scrapy
from scrapy.loader import ItemLoader
from School_News.items import DmozItem
from parsel.selector import Selector



class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["hao123.com"]
    start_urls = [
        "http://www.hao123.com/edu"
    ]

    def parse(self, response):
        College_level = []
        for lever in response.xpath('//div[@class="edu-container"]//tr[1]/th[position()>1]'):
            College_level.append(lever.xpath('text()').extract())
        for city in response.xpath('//div[@class="edu-container"]//tr/td[@class="first"]/..'):
            province = city.xpath('td[@class="first"]/text()').extract()
            for index, College_category in enumerate(city.xpath('td/a/..')):
                l = ItemLoader(item=DmozItem(), selector=College_category, response=response)
                l.add_value('province', province)
                l.add_xpath('link', 'a/@href')
                l.add_xpath('College_sum', 'text()[1]')
                l.add_value('College_level', College_level[index])

                yield l.load_item()

    #     yield from self.parse_list(response)
    #
    # def parse_list(self, response):
    #     for sel in response.xpath('//div[@class="t1 bgg"]'):
    #         item = DmozItem()
    #         item['title'] = sel.xpath('.//a/text()').extract()
    #         item['link'] = sel.xpath('.//a/@href').extract()
    #         print(item['title'], item['link'])
    #         yield item
    #
    #
    #     for index, li in enumerate(response.xpath(self.config.item_container_xpath)):
    #         l = ItemLoader(selector=li, response=response)
    #         link_fragment = None
    #         for prop in self.config.item_properties:
    #             if prop.name == 'url':
    #                 link_fragment = li.xpath('.//a').extract_first()
    #             if prop.name == 'group':
    #                 l.add_value(prop.name, group)
    #             elif prop.name in ['url', 'title', 'publish_time'] and prop.xpath:
    #                 l.add_xpath(prop.name, prop.xpath)