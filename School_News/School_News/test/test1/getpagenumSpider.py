from scrapy import Spider
import re
from scrapy.http import HtmlResponse
from selenium import webdriver


class xxxSpider(Spider):
    allowed_domains = ["hnjxw.gov.cn"]
    start_urls = [
        'http://www.hnjxw.gov.cn/xxgk_71033/jgzn/jgzn/',
        'http://www.hnjxw.gov.cn/xxgk_71033/jgzn/nsjg/',
    ]

    # def start_requests(self):
    #     browser = webdriver.Chrome()
    #     for i in self.start_urls:
    #         browser.get(url=i)
    #         yield HtmlResponse(browser.current_url,
    #                            body=browser.page_source,
    #                            encoding='utf-8',
    #                            )

    def parse(self, response):
        # a = response.xpath('//div[@class="manu"]/span[1]/b/text()').extract_first()
        # b = response.xpath('substring-after(//div[@class="manu"]/span[2]/text()[2], "/")').extract_first()
        a = response.xpath('//p[@class="pages"]/span[2]/text()').extract_first()
        b = response.xpath('//p[@class="pages"]/span[3]/text()').extract_first()

        # a = response.xpath(
        #     'substring-before(substring-after(//*[contains(text(),"共") and (contains(text(),"条") or contains(text(),"页"))]/../text()'
        #     ', "共"),"页")').extract_first()
        # b = response.xpath(
        #     'substring-before(substring-after(//*[contains(text(),"共") and (contains(text(),"条") or contains(text(),"页"))]/../text()'
        #     ', "   共"),"篇")').extract_first()
        r = response.xpath(
            '//div[@class="Pages"]//a').extract()
        try:
            print(r)
        except:
            pass
        if a == None:
            a = 0
        if b == None:
            b = 0
        a = re.sub("\D", "", a)
        b = re.sub("\D", "", b)
        print(a, '-', b)
        self.he(a, b)

    c = 0
    d = 0

    def he(self, a, b):
        try:
            self.c = self.c + int(a.strip())
            self.d = self.d + int(b.strip())
        except:
            self.c = 0
            self.d = 0
        print(self.c, '--', self.d)
        f = '{},{},{},{}\n'.format(a, b, self.c, self.d)
        file_object = open('C:/Users/yf/Desktop/sum/{}.txt'.format(self.allowed_domains[0]), 'a')
        file_object.write(f)
        file_object.close()
