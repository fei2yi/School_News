from scrapy.http import Request
from scrapy.loader import ItemLoader
from scrapy import Spider


class CollegeNewsSpider(Spider):
    name = 'CollegeNews'
    allowed_domains = ['pku.edu.cn']
    start_urls = [
        'http://www.pku.edu.cn/',  # 国务院文件专栏
    ]

    def parse(self, response):
        urls = response.xpath('.....')
        for url in urls:
            request = Request(url=url, callback=self.parse_post, dont_filter=True)
            request.meta['PhantomJS'] = True
            yield request

    def parse_post(self, response):
         """
        解析文章正文页
        """

