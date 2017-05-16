from scrapy.http import Request
from School_News.items import EachPagesLinkItem
from School_News.lib.loader import EachPagesLinkLoader
from scrapy import Spider
from School_News.lib.transporturl import transport
import pymysql


class ArticleSpider(Spider):
    name = 'article'
    allowed_domains = []
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='yyaiyi',
                           db='school_news',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM eachlistlinkitem a")

    a = cursor.fetchall()
    start_urls = [[i.get('listUrl'), i.get('list'), i.get('xpath'), i.get('parent')] for i in a]

    def start_requests(self):
        for urll in self.start_urls:
            url = urll[0]
            request = Request(url, meta={'listUrl': url, 'list': urll[1], 'xpath': urll[2], 'parent': urll[3]})
            # request.meta['PhantomJS'] = True
            yield request

    def parse(self, response):
        yield from self.nextpage(response)

    num = 0

    def nextpage(self, response):
        self.num += 1
        a = [['a', 300], ['div', 20], ['span', 5]]
        b = [['text()', 269], ['@title', 50], ['@class', 30], ['@href', 10]]
        c = [['下一页', 172], ['下页', 60], ['后页', 40], ['next', 30], ['Next', 30]]
        xpath = '//{}[contains({},"{}")]/@href'
        xpaths = []

        for i in a:
            for o in b:
                for p in c:
                    xp = xpath.format(i[0], o[0], p[0])
                    wg = i[1] * o[1] * p[1]
                    xpaths.append([xp, wg])
        xpaths = sorted(xpaths, key=lambda d: d[1], reverse=True)
        wgl = []
        for x in xpaths:
            sele = response.xpath(x[0]).extract_first()
            if sele:
                url = response.urljoin(sele)
                if self.Homepage(url):
                    print('是主页，应该删掉', url)
                else:
                    wgl.append([sele, x[1], x])
            elif x[0] == '//span[contains(text(),"下一页")]/@href':
                sele = response.xpath('//span[contains(text(),"下一页")]/../@href').extract_first()
                if sele:
                    wgl.append([sele, x[1], x])
        if len(wgl) > 0:
            wgy = sorted(wgl, key=lambda d: d[1], reverse=True)[0]
            url = response.urljoin(wgy[0])
            if 'javascript' in url:
                print('最后一页或此分页需点击:', response.url)
            else:
                print('url:', url, wgy[0], '权重:', wgy[1])

                epll = EachPagesLinkLoader(item=EachPagesLinkItem())
                epll.add_value('pageUrl', url)
                epll.add_value('pageNum', str(self.num))
                epll.add_value('pageSum', '浏览器')
                epll.add_value('parent', response.meta.get('parent'))
                epllitme = epll.load_item()
                yield epllitme
                yield Request(url, callback=self.parse, dont_filter=False, meta={'next_page': True})
        elif response.meta.get("next_page"):
            print('最后一页：', response.url)
        elif '用浏览器':
            print('用浏览器', response.url)
            epll = EachPagesLinkLoader(item=EachPagesLinkItem(), response=response)
            epll.add_value('pageUrl', response.url)
            epll.add_value('pageNum', self.num)
            epll.add_value('pageSum', 1)
            epll.add_value('parent', response.url)
            epllitme = epll.load_item()
            yield epllitme
        elif '无下一页，却有一排页码':
            print('无下一页，却有一排页码', response.url)
        elif '真正的无分页':
            print('真正的无分页：', response.url)


            # print(url)
            # request = Request(url, callback=self.parse, meta={'parent_temp': response.meta.get('parent_temp')},
            #                   dont_filter=False)
            # request.meta['PhantomJS'] = True
            # yield request

    def Homepage(self, url):
        b = url.split('.')
        if 'edu' in b and ('cn/' in b or 'cn' in b) and 'http://news' in b and len(b) == 4:
            return True
        elif 'edu' in b and 'cn/index' in b and 'http://news' in b and len(b) == 5:
            return True
        elif 'com' in b and 'http://news' in b and len(b) == 3:
            return True
        else:
            return False
