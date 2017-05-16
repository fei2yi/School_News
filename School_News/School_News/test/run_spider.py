from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from School_News.spiders.Article import ArticleSpider

# from School_News.spiders.test.getpagenumSpider import xxxSpider


process = CrawlerProcess(get_project_settings())
# process.crawl(ListPageCollectSpider)
process.crawl(ArticleSpider)
# process.crawl(xxxSpider)
process.start()
