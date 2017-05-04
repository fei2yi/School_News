from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from School_News.spiders.GzcoalSpider import GzcoalSpider
from School_News.spiders.school_new import DmozSpider


process = CrawlerProcess(get_project_settings())
process.crawl(DmozSpider)
process.start()
