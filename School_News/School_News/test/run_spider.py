from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from School_News.spiders.WebsiteCollect import WebsiteCollectSpider
# from School_News.spiders.text_submit_data import LoginSpider

process = CrawlerProcess(get_project_settings())
process.crawl(WebsiteCollectSpider)
# process.crawl(LoginSpider)
process.start()
