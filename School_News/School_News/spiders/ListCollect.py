from scrapy.http import Request
from School_News.items import EachListLinkItem
from School_News.lib.loader import EachListLinkLoader
from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from School_News.lib.transporturl import transport


class ListCollectSpider(CrawlSpider):
    name = 'ListCollect'
    allowed_domains = []
    start_urls = [i for i in transport('WebsiteCollect.json', 'link')]

    rules = (
        Rule(LinkExtractor(allow=('(.*)xwzh_(.*)',)), callback='parse_item', follow=True),
        #元素//a[contains(text(),"新闻")]
        # 元素//a[contains(text(),"要闻")]
        # 元素//a[contains(text(),"动态")]
        # 元素//a[contains(text(),"新闻")]
        # 元素//a[contains(text(),"新闻")]
        # 元素//a[contains(text(),"新闻")]
        # 元素//a[contains(text(),"新闻")]
        # 元素//a[contains(text(),"新闻")]

    )

    def parse_start_url(self, response):
            request = Request(response.url)
            # request.meta['PhantomJS'] = True
            yield request

    def parse_item(self, response):
        listUrls = response.xpath('//*[contains(text(),"通知") or contains(text(),"要闻") or contains(text(),"动态")'
                                  ' or contains(text(),"新闻") or contains(text(),"科研") or contains(text(),"公告")]/../..//a'
                                  '|//*[contains(@href,"/tzgg") or contains(@href,"news") or contains(@href,"xww") or contains(@href,"/gzdt")'
                                  ' or contains(@href,"/xzhd/")]')

        for url in listUrls:
            elll = EachListLinkLoader(item=EachListLinkItem(), selector=url, response=response)
            elll.add_xpath('listUrl', '@href')
            elll.add_xpath('list', 'text()')
            elll.add_value('parent', response.url)
            ealiitme = elll.load_item()
            if 'list' not in ealiitme.keys() or 'listUrl' in ealiitme.keys() and len(ealiitme['list']) < 5:
                yield ealiitme

                #         request = Request(url=url, callback=self.parse_post, dont_filter=True)
                #         request.meta['PhantomJS'] = True
                #         yield request
                #
                # def parse_post(self, response):
                #      """
                #     解析文章正文页
                #     """
