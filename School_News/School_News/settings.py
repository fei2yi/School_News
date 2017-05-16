# -*- coding: utf-8 -*-

# Scrapy settings for School_News project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'School_News'

SPIDER_MODULES = ['School_News.spiders']
NEWSPIDER_MODULE = 'School_News.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'School_News (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)


# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1  # 下载延迟
RANDOMIZE_DOWNLOAD_DELAY = True
CRAWLERA_PRESERVE_DELAY = True

# DEFAULT_REQUEST_HEADERS = {
#
#     # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#
#     # 'Accept-Language': 'zh-CN,zh;q=0.8',
#
#     'X-Crawlera-Cookies': 'disable'
#
# }
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)





# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False






# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html


# DELTAFETCH_ENABLED = True
# MAGICFIELDS_ENABLED = True
# MAGIC_FIELDS = {
#     "timestamp": "$time",
#     "spider": "$spider:name",
#     "url": "scraped from $response:url",
#     "domain": "$response:url,r'https?://([\w\.]+)/']",
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html



# CRAWLERA_ENABLED = True
#
# CRAWLERA_USER = '<51d2d2a480e046c6b6c370cb8e52e4c9>'
#
# CRAWLERA_PASS = 'yyaiyi.sh'
# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html


FEED_URI = '%(file_path)s%(name)s-%(time)s%(feed_fromat)s'
FEED_FORMAT = 'json'
FEED_EXPORT_ENCODING = 'utf-8'

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html


# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False


# start MySQL database configure setting
# end of MySQL database configure setting

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#启用在redis中调度存储请求队列。
# SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
#确保所有蜘蛛共享相同的重复项通过redis过滤。
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#不要清理redis队列，允许暂停/恢复爬网。
#SCHEDULER_PERSIST = True

# 种子队列的信息
REDIE_URL = None
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

# 去重队列的信息
# FILTER_URL = None
# FILTER_HOST = 'localhost'
# FILTER_PORT = 6379
# FILTER_DB = 0

ITEM_PIPELINES = {
    'School_News.pipelines.SchoolNewsPipeline': 300,
    'School_News.pipelines.MySQLDBPipeline': 302,
    # 'scrapy_redis.pipelines.RedisPipeline': 300,
}

DOWNLOADER_MIDDLEWARES = {
    'School_News.lib.JSMiddleware.PhantomJSMiddleware': 100,
    # 'School_News.middlewares.MyCustomDownloaderMiddleware': 543,
    # 'scrapy_crawlera.CrawleraMiddleware': 600
    # "School_News.middlewares.UserAgentMiddleware": 401,#用户代理
    # "Sina_spider3.middleware.CookiesMiddleware": 402,
}

EXTENSIONS = {
    'scrapy.extensions.telnet.TelnetConsole': None,
    'scrapy.extensions.feedexport.FeedExporter': None,
    # 'School_News.lib.feedexport.School_newsFeedExporter': 1,
}

SPIDER_MIDDLEWARES = {
    # 'scrapy_deltafetch.DeltaFetch': 50,
    # 'scrapy_magicfields.MagicFieldsMiddleware': 51,
    # 'School_News.middlewares.SchoolNewsSpiderMiddleware': 543,
}

#广泛抓取
COOKIES_ENABLED = False   #禁用Cookie
RETRY_ENABLED = False   #禁用重试
REDIRECT_ENABLED = False   #禁用重定向
DOWNLOAD_TIMEOUT = 15  #减少下载超时
LOG_LEVEL = 'INFO'   #降低日志级别
CONCURRENT_REQUESTS = 20   #增加全局并发请求数
REACTOR_THREADPOOL_MAXSIZE = 20  #增加Twisted IO线程池的最大大小

