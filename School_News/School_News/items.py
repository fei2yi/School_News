# -*- coding: utf-8 -*-
from scrapy.item import Item, Field


class City(Item):
    province = Field()
    link = Field()
    collegeSum = Field()
    collegeLevel = Field()

class College(Item):
    name = Field()
    url = Field()
    parent = Field()

class Listtemp(Item):
    list = Field()
    listUrl = Field()

    parent = Field()

class List(Item):
    list = Field()
    listUrl = Field()
    xpath = Field()
    parent = Field()

class Page(Item):
    pageUrl = Field()
    pageNum = Field()
    pageSum = Field()
    parent = Field()

class Article(Item):
    title = Field()
    textUrl = Field()
    publishTime = Field()
    parent = Field()

class Content(Item):
    author = Field()
    source = Field()
    publishTime = Field()
    content = Field()
    fileUrls = Field()
    filePaths = Field()
    fileNames = Field()
    parent = Field()
    crawl=Field()
