import scrapy
from scrapy.http import Request
from School_News.items import City, College
from School_News.lib.loader import CityLoader, CollegeLoader


class WebsiteSpider(scrapy.Spider):
    name = "Website"
    allowed_domains = ["hao123.com", "baidu.com"]
    start_urls = [
        "http://www.hao123.com/edu"
    ]

    def parse(self, response):
        College_level = []
        for lever in response.xpath('//div[@class="edu-container"]//tr[1]/th[position()>1]'):
            College_level.append(lever.xpath('text()').extract())
        for ct in response.xpath('//div[@class="edu-container"]//tr/td[@class="first"]/..'):
            province = ct.xpath('td[@class="first"]/text()').extract()
            for index, College_category in enumerate(ct.xpath('td/a/..')):
                cci = CityLoader(item=City(), selector=College_category, response=response)
                cci.add_value('province', province)
                cci.add_xpath('link', 'a/@href')
                cci.add_xpath('collegeSum', 'text()[1]')
                cci.add_value('collegeLevel', College_level[index])
                cciitme = cci.load_item()
                yield cciitme

                request = Request(cciitme['link'], callback=self.parse_list)
                # request.meta['PhantomJS'] = True
                yield request

    def parse_list(self, response):
        for li in response.xpath('//tr[@bgcolor="#EFF7F0"]'):
            cwi = CollegeLoader(item=College(), selector=li)
            cwi.add_xpath('name', './/a/text()')
            cwi.add_xpath('url', './/a/@href')
            cwi.add_value('parent', response.url)
            cwiitme = cwi.load_item()
            if 'name' not in cwiitme.keys():
                cwi.add_xpath('name', './/p/text()')
                cwiitme = cwi.load_item()
            if 'url' not in cwiitme.keys() or 'baike.baidu' in cwiitme['url']:
                scrapy.FormRequest(url="https://www.baidu.com/",
                                   formdata={'wd': cwiitme['name']},
                                   callback=self.parse_baidu_result,
                                   meta={'name': cwiitme['name']})
            else:
                yield cwiitme

    def parse_baidu_result(self, response):
        href = response.xpath('//a[text()="官网"][1]/../a[1]/@href').extract()
        yield Request(href, callback=self.real_web_address, meta={'name': response.meta['name']})

    def real_web_address(self, response):
        name = response.meta['name']
        href = response.xpath('substring-before(substring-after(//script/text(),\'replace("\'), \'")}\')').extract()
        cwi = CollegeLoader(item=College())
        cwi.add_value('name', name)
        cwi.add_value('url', href)
        cwiitme = cwi.load_item()
        yield cwiitme
