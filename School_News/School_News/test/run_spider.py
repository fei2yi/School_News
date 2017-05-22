from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from School_News.spiders.Articlezl import ArticleItemSpider

# from School_News.spiders.test.getpagenumSpider import xxxSpider


process = CrawlerProcess(get_project_settings())
# process.crawl(ListPageCollectSpider)
process.crawl(ArticleItemSpider)
# process.crawl(xxxSpider)
process.start()
