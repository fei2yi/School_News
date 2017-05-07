from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from School_News.spiders.WebsiteCollect import WebsiteCollectSpider
# from School_News.spiders.zzzzzz import SegSpider
from School_News.spiders.ListPageCollect import ListPageCollectSpider


process = CrawlerProcess(get_project_settings())
# process.crawl(ListPageCollectSpider)
process.crawl(WebsiteCollectSpider)
# process.crawl(SegSpider)
process.start()
