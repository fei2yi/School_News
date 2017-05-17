from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Identity
from School_News.items import CollegeCityItem, CollegeWebItem, EachArticleLinkItem, ArticleContentItem, \
    EachListLinkItem, EachListtempItem, EachPagesLinkItem


def urljoin(url, loader_context):
    response = loader_context.get('response')
    if 'http' in url:
        return url
    else:
        return response.urljoin(url)


class CollegeCityLoader(ItemLoader):
    default_output_processor = TakeFirst()

    province_in = MapCompose(str.strip)
    link_in = MapCompose(str.strip, urljoin)
    collegeSum_in = MapCompose(str.strip)
    collegeLevel_in = MapCompose(str.strip)

    def __init__(self, item=None, selector=None, response=None, parent=None, **context):
        item = item or CollegeCityItem()
        super(CollegeCityLoader, self).__init__(item, selector, response, parent, **context)


class CollegeWebLoader(ItemLoader):
    default_output_processor = TakeFirst()

    name_in = MapCompose(str.strip)
    url_in = MapCompose(str.strip)
    parent_in = MapCompose(str.strip)

    def __init__(self, item=None, selector=None, response=None, parent=None, **context):
        item = item or CollegeWebItem()
        super(CollegeWebLoader, self).__init__(item, selector, response, parent, **context)


class EachListtempLoader(ItemLoader):
    default_output_processor = TakeFirst()

    list_in = MapCompose(str.strip)
    listUrl_in = MapCompose(str.strip, urljoin)
    parent_in = MapCompose(str.strip)

    def __init__(self, item=None, selector=None, response=None, parent=None, **context):
        item = item or EachListtempItem()
        super(EachListtempLoader, self).__init__(item, selector, response, parent, **context)


class EachListLinkLoader(ItemLoader):
    default_output_processor = TakeFirst()

    list_in = MapCompose(str.strip)
    listUrl_in = MapCompose(str.strip, urljoin)
    xpath_in = MapCompose(str.strip)
    parent_in = MapCompose(str.strip)

    def __init__(self, item=None, selector=None, response=None, parent=None, **context):
        item = item or EachListLinkItem()
        super(EachListLinkLoader, self).__init__(item, selector, response, parent, **context)


class EachPagesLinkLoader(ItemLoader):
    default_output_processor = TakeFirst()

    pageUrl_in = MapCompose(str.strip)
    pageSum_in = MapCompose(str.strip)
    pageNum_in = MapCompose(str.strip)
    parent_in = MapCompose(str.strip)

    def __init__(self, item=None, selector=None, response=None, parent=None, **context):
        item = item or EachPagesLinkItem()
        super(EachPagesLinkLoader, self).__init__(item, selector, response, parent, **context)


class EachArticleLinkLoader(ItemLoader):
    default_output_processor = TakeFirst()

    title_in = MapCompose(str.strip)
    textUrl_in = MapCompose(str.strip, urljoin)
    publishTime_in = MapCompose(str.strip)
    parent_in = MapCompose(str.strip, urljoin)

    def __init__(self, item=None, selector=None, response=None, parent=None, **context):
        item = item or EachArticleLinkItem()
        super(EachArticleLinkLoader, self).__init__(item, selector, response, parent, **context)


class ArticleContentLoader(ItemLoader):
    default_output_processor = TakeFirst()

    author_in = MapCompose(str.strip)
    source_in = MapCompose(str.strip)
    publishTime_in = MapCompose(str.strip)
    content_in = MapCompose(str.strip)
    fileUrls_in = MapCompose(str.strip)
    filePaths_in = MapCompose(str.strip)
    fileNames_in = MapCompose(str.strip)
    parent_in = MapCompose(str.strip, urljoin)

    file_urls_out = Identity()

    def __init__(self, item=None, selector=None, response=None, parent=None, **context):
        item = item or ArticleContentItem()
        super(ArticleContentLoader, self).__init__(item, selector, response, parent, **context)
