# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class CollegeCityItem(Item):
    province = Field()
    link = Field()
    collegeSum = Field()
    collegeLevel = Field()


class CollegeWebItem(Item):
    name = Field()
    url = Field()


class EachArticleLinkItem(Item):
    group = Field()
    groupUrl = Field()

    title = Field()
    textUrl = Field()
    publishTime = Field()


class ArticleContentItem(Item):
    author = Field()
    source = Field()
    publishTime = Field()
    content = Field()
    fileUrls = Field()
    filePaths = Field()
    fileNames = Field()
