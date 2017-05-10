from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from School_News.spiders.test.getpagenumSpider import xxxSpider

process = CrawlerProcess(get_project_settings())
process.crawl(xxxSpider)
process.start()
