from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from School_News.spiders.ListCollect2 import ListCollect2Spider

# from School_News.spiders.test.getpagenumSpider import xxxSpider


process = CrawlerProcess(get_project_settings())
# process.crawl(ListPageCollectSpider)
process.crawl(ListCollect2Spider)
# process.crawl(xxxSpider)
process.start()
