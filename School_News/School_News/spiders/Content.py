# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
import pymysql
from School_News.items import Content
from School_News.lib.loader import ContentLoader


class ContentSpider(Spider):
    name = 'content'
    allowed_domains = []
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='yyaiyi',
                           db='school_news',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT a.textUrl FROM eacharticlelinkitem a LEFT JOIN articlecontentitem b ON a.textUrl=b.parent"
            "WHERE crawl!='yes'")
    except:
        cursor.execute("SELECT textUrl FROM eacharticlelinkitem")

    a = cursor.fetchall()
    start_urls = [i.get('textUrl') for i in a]

    def start_requests(self):
        for url in self.start_urls:
            request = Request(url)
            # request.meta['PhantomJS'] = True
            yield request

    def parse(self, response):
        content = self.get_con(response)
        if content:
            acl = ContentLoader(item=Content(), response=response)
            acl.add_value('author', 'no')
            acl.add_value('source', 'no')
            acl.add_value('publishTime', 'no')
            acl.add_value('content', content)
            acl.add_value('fileUrls', 'no')
            acl.add_value('filePaths', 'no')
            acl.add_value('fileNames', 'no')
            acl.add_value('crawl', 'yes')

            acl.add_value('parent', response.url)
            aclitme = acl.load_item()
            print(response.url, content)
            yield aclitme
        else:
            print("未获取到内容:", response.url)

    def get_con(self, response):
        a = [['div', 262], ['td', 33], ['table', 16], ['font', 8], ['p', 8]]
        b = [['class', 223], ['id', 88]]
        c = [['TRS_Editor', 50], ['content', 46], ['zoom', 21], ['con', 15], ['article', 15], ['text', 13],
             ['Zoom', 12], ['info_content', 8]]
        xpaths = []
        for i in a:
            for o in b:
                for p in c:
                    xpath = "//{}[contains(@{},'{}')]".format(i[0], o[0], p[0])
                    weiget = i[1] * o[1] * p[1]
                    xpaths.append([xpath, weiget])
        xpaths = sorted(xpaths, key=lambda d: d[1], reverse=True)
        wgl = []
        for x in xpaths:
            sel = response.xpath(x[0])
            if sel:
                wgl.append([sel, x[1], x[0]])
        if wgl:
            wgy = sorted(wgl, key=lambda d: d[1], reverse=True)[0]
            content = wgy[0].extract_first()
            return content
        else:
            return False
