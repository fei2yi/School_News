import scrapy
from scrapy.loader import ItemLoader
from School_News.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["hao123.com"]
    start_urls = [
        "http://www.hao123.com/edu"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="t1 bgg"]'):
            item = DmozItem()
            item['title'] = sel.xpath('.//a/text()').extract()
            item['link'] = sel.xpath('.//a/@href').extract()
            print(item['title'], item['link'])
            yield item
        yield from self.parse_list(response)

    def parse_list(self, response):
        for index, li in enumerate(response.xpath(self.config.item_container_xpath)):
            l = ItemLoader(selector=li, response=response)
            link_fragment = None
            for prop in self.config.item_properties:
                if prop.name == 'url':
                    link_fragment = li.xpath('.//a').extract_first()
                if prop.name == 'group':
                    l.add_value(prop.name, group)
                elif prop.name in ['url', 'title', 'publish_time'] and prop.xpath:
                    l.add_xpath(prop.name, prop.xpath)