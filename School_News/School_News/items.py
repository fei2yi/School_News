# -*- coding: utf-8 -*-
from scrapy.item import Item, Field


class CollegeCityItem(Item):
    province = Field()
    link = Field()
    collegeSum = Field()
    collegeLevel = Field()


class CollegeWebItem(Item):
    name = Field()
    url = Field()
    parent = Field()

class EachListtempItem(Item):
    list = Field()
    listUrl = Field()

    parent = Field()

class EachListLinkItem(Item):
    list = Field()
    listUrl = Field()
    xpath = Field()
    parent = Field()


class EachPagesLinkItem(Item):
    pageUrl = Field()
    pageNum = Field()
    pageSum = Field()
    parent = Field()


class EachArticleLinkItem(Item):
    title = Field()
    textUrl = Field()
    publishTime = Field()
    parent = Field()


class ArticleContentItem(Item):
    author = Field()
    source = Field()
    publishTime = Field()
    content = Field()
    fileUrls = Field()
    filePaths = Field()
    fileNames = Field()
    parent = Field()
