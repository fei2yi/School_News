# -*- coding: utf-8 -*-

from scrapy.extensions.feedexport import FeedExporter
from School_News.lib.environment import env


# class School_newsFeedExporter(FeedExporter):
#     def _get_uri_params(self, spider):
#         params = super(School_newsFeedExporter, self)._get_uri_params(spider)
#         params['file_path'] = 'file:///{}/'.format(env.result_path)
#         params['feed_fromat'] = spider.crawler.settings.get('FEED_FORMAT')
#         params['feed_fromat'] = '.{}'.format(params['feed_fromat']) if params['feed_fromat'] else ''
#         return params
