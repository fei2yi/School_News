from scrapy.http import Request
from School_News.items import EachListLinkItem
from School_News.lib.loader import EachListLinkLoader
from scrapy import Spider
from School_News.lib.transporturl import transport
import pymysql


class ListCollect2Spider(Spider):
    name = 'ListCollect2'
    allowed_domains = []
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='yyaiyi',
                           db='school_news',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM eachlisttempitem a")

    a = cursor.fetchall()
    start_urls = [[i.get('listUrl'), i.get('list'), i.get('parent')] for i in a]

    def start_requests(self):
        for urll in self.start_urls:
            url = urll[0]
            request = Request(url, meta={'listUrl': url, 'list': urll[1], 'parent': urll[2]})
            # request.meta['PhantomJS'] = True
            yield request

    def parse(self, response):
        resl = self.secondejudge(response)
        url = response.meta.get('listUrl')
        text = response.meta.get('list')
        parent = response.meta.get('parent')
        if isinstance(resl, list):
            xpath = '{}#{}#{}'.format(resl[0], resl[1], resl[2], )
            elll = EachListLinkLoader(item=EachListLinkItem(), response=response)
            elll.add_value('listUrl', url)
            elll.add_value('list', text)
            elll.add_value('parent', parent)
            elll.add_value('xpath', xpath)
            elllitme = elll.load_item()
            yield elllitme

    def secondejudge(self, response):
        a = [{'div': 126}, {'ul': 66}, {'table': 56}, {'td': 32}, {'tr': 12}]
        b = [{'li': 112}, {'tr': 41}, {'td': 10}, {'div': 7}, {'ul': 6}, {'table': 6}, {'a': 5}]
        xpath = '//{}/{}//a[@target]/ancestor::{}'
        xpaths = []
        # body_num = response.xpath("//body/*")
        # if len(body_num) >= 3:
        #     resp1=response.xpath("//body/*[position()>1 and position()<last()]")
        for i in a:
            for p in b:
                xp = xpath.format(list(i.keys())[0], list(p.keys())[0], list(i.keys())[0])
                wg = list(i.values())[0] * list(p.values())[0]
                xpaths.append({xp: wg})
        xpaths = sorted(xpaths, key=lambda d: list(d.values()), reverse=True)
        wgl = []
        for x in xpaths:

            sel = response.xpath(list(x.keys())[0])
            if sel:
                wgl.append([sel, list(x.values())[0], x])
        if wgl:
            wgy = sorted(wgl, key=lambda d: d[1], reverse=True)[0]
            x_xpa = list(wgy[2].keys())[0]
            print('xpath:', x_xpa, '权重:', wgy[1], 'ancestor_a:', len(wgy[0]))
            # 以上实现了xpath最大权重的过滤，但会匹配多个祖宗，需要再次判别提取一层元素。
            l = x_xpa.split('/')[3]
            xpath2 = '{}'.format(l)
            # //a[@target]/ancestor::{}[1], l
            result_path = []
            for i in range(0, len(wgy[0])):
                sel2 = wgy[0][i].xpath(xpath2)
                print(i, 'xpath2:', xpath2, len(sel2), sel2)
                result_path.append([x_xpa, i, xpath2, len(sel2)])
            result_path1 = sorted(result_path, key=lambda d: d[3], reverse=True)[0]
            if result_path1[3] in [5, 10, 12, 15, 20, 21, 22, 23, 24, 25, 30, ]:
                print('精确规则的匹配：', result_path1[0], result_path1[1], result_path1[2])
                return [result_path1[0], result_path1[1], result_path1[2]]
            if result_path1[3] > 10:
                print('大于10规则的匹配：', result_path1[0], result_path1[1], result_path1[2])
                return [result_path1[0], result_path1[1], result_path1[2]]
