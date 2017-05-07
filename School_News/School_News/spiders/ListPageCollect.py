from scrapy.http import Request
from School_News.items import EachListLinkItem
from School_News.lib.loader import EachListLinkLoader
from scrapy import Spider
from School_News.lib.transporturl import transport


class ListPageCollectSpider(Spider):
    name = 'ListPage'
    allowed_domains = []
    start_urls = [i for i in transport('WebsiteCollect.json', 'url')]

    def start_requests(self):
        for start_url in self.start_urls:
            request = Request(start_url)
            # request.meta['PhantomJS'] = True
            yield request

    def parse(self, response):
        listUrls = response.xpath('//*[contains(text(),"通知") or contains(text(),"要闻") or contains(text(),"动态")'
                                  ' or contains(text(),"新闻") or contains(text(),"科研") or contains(text(),"公告")]/../..//a'
                                  '| //span[contains(text(),"通知") or contains(text(),"要闻") or contains(text(),"动态")'
                                  ' or contains(text(),"新闻") or contains(text(),"科研") or contains(text(),"公告")]/..//a'
                                  '| //*[contains(@href,"/tzgg") or contains(@href,"news") or contains(@href,"xww") or contains(@href,"/gzdt")'
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
