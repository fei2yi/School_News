from scrapy.linkextractors import LinkExtractor
import scrapy
# from scrapy import spider
from scrapy.spiders import CrawlSpider, Rule


class JudgelistSpider(scrapy.Spider):
    name = 'judgelist'
    allowed_domains = []
    start_urls = [
        # 'http://www.ah.gov.cn/UserData/SortHtml/1/68419472402.html',
        'http://www.aheic.gov.cn/zwgk/zwgk_list.jsp?strColId=13748052639067468&view_type=4',

    ]

    def parse(self, response):
        a = [{'div': 126}, {'ul': 66}, {'table': 56}, {'td': 32}, {'tr': 12}]
        b = [{'li': 112}, {'tr': 41}, {'td': 10}, {'div': 7}, {'ul': 6}, {'table': 6}, {'a': 5}]
        xpath = '//{}/{}//a[@target]/ancestor::{}'
        xpaths = []

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
            wgl = sorted(wgl, key=lambda d: d[1], reverse=True)[0]
            print('xpath:', wgl[2], '权重:', wgl[1], 'sel:', len(wgl[0]))
            l = list(wgl[2].keys())[0].split('/')[3]
            xpath2 = '{}//a/ancestor::{}[1]'.format(l, l)
            # //a/ancestor::{}, l
            for i in range(0, len(wgl[0])):
                sel2 = wgl[0][i].xpath(xpath2)
                print(i, 'xpath2:', xpath2, len(sel2), sel2)
