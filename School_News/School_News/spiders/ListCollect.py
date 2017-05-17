from scrapy.http import Request
from School_News.items import EachListtempItem
from School_News.lib.loader import EachListtempLoader
from scrapy import Spider
from School_News.lib.transporturl import transport
import pymysql


class ListCollectSpider(Spider):
    name = 'ListCollect'
    allowed_domains = []
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='yyaiyi',
                           db='school_news',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    cursor.execute("SELECT b.url FROM collegecityitem a INNER "
                   "JOIN collegewebitem b ON a.link = b.parent WHERE collegeLevel='普通本科院校(908所)'")

    a = cursor.fetchall()
    start_urls = [i.get('url') for i in a]

    def start_requests(self):
        for url in self.start_urls:
            request = Request(url, meta={'parent_temp': url})
            request.meta['PhantomJS'] = True
            yield request

    def parse(self, response):
        resl = self.firstchoose(response)
        for url_text in resl:
            url = url_text[0]
            text = url_text[1]
            if url not in [i.get('listUrl') for i in self.b]:
                eltl = EachListtempLoader(item=EachListtempItem(), response=response)
                eltl.add_value('listUrl', url)
                eltl.add_value('list', text)
                eltl.add_value('parent', response.meta.get('parent_temp'))
                eltlitme = eltl.load_item()
                yield eltlitme
                print(url)
                request = Request(url, callback=self.parse, meta={'parent_temp': response.meta.get('parent_temp')},
                                  dont_filter=False)
                request.meta['PhantomJS'] = True
                yield request

    def firstchoose(self, response):
        a = [['a', 50], ['span', 3]]
        b = [['text()', 50], ['@href', 3], ['@title', 2]]
        c = [['\"新闻\"', 195], ['\"要闻\"', 114], ['\"动态\"', 555], ['\"通知\"', 169], ['\"头条\"', 50], ['\"更多\"', 100],
             ['\"more\"', 120], ['\"MORE\"', 20], ['\"http://news.\"', 30]]

        xpaths = []
        for i in a:
            for o in b:
                for p in c:
                    xpath = '//{}[contains({},{})]'.format(i[0], o[0], p[0])
                    weiget = i[1] * o[1] * p[1]
                    xpaths.append([xpath, weiget])
        xpaths = sorted(xpaths, key=lambda d: d[1], reverse=True)
        resl = []
        for x in xpaths:
            try:
                res = response.xpath(x[0] + '/@href').extract_first()
            except:
                res = None
            try:
                res_text = response.xpath(x[0] + '/text()').extract_first()
            except:
                res_text = 'null'
            if not res_text:
                res_text = 'null'
            if res:
                res = response.urljoin(res)
                if len(res_text) < 6 and '网' not in res_text:
                    res_d = [res, res_text]
                    resl.append(res_d)
        return resl
