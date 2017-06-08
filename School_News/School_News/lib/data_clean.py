# coding=gbk
import re
from School_News.lib.ex import *
from bs4 import BeautifulSoup, Tag, NavigableString


def save_html(html):
    html = BeautifulSoup(html, 'lxml').prettify()
    with open('saved.html', 'w', encoding='utf8') as f:
        f.write(html)


def extract_text(node, text_re=None):
    html = BeautifulSoup(iter_tree(node, text_re), 'lxml').text
    return re.sub('\s+', ' ', html)


def tag_factor(ele):
    if ele.name in ['meta', 'head', 'style', 'script', 'img']:
        return
    tag_attr = [
        (['table', 'thead', 'tbody', 'tfoot', 'th', 'tr', 'td'],
         ['style', 'align', 'valign', 'width', 'colspan', 'rowspan']),
        # (['img'],
        # ['width', 'height', 'src'])
    ]
    tag_attr = {k: vs for ks, vs in tag_attr for k in ks}
    dict2attrs = lambda d: ' '.join(['{}="{}"'.format(k, v) for k, v in d.items()])
    attrs = {k: ' '.join(v) if isinstance(v, list) else v for k, v in ele.attrs.items() if k in tag_attr[ele.name]} \
        if ele.name in tag_attr else {}
    return {'tag': ele.name, 'attrs': dict2attrs(attrs)}


def iter_tree(ele, text_re=None):
    if type(ele) is Tag:
        factor = tag_factor(ele)
        if not factor:
            return ''
        factor['content'] = ''.join([iter_tree(c, text_re) for c in ele.contents])
        factor['attrs_space'] = ' ' if factor['attrs'] else ''
        return '<{tag}{attrs_space}{attrs}>{content}</{tag}>'.format(**factor)
    elif type(ele) is NavigableString:
        text = str(ele)
        return '' if text_re and re.search(text_re, text) else text
    else:
        return ''


# b = get('http://dbj.nea.gov.cn/ywdt/201703/t20170316_2813095.html')

# text=''
# soup = BeautifulSoup(text, 'lxml')
# node = soup.find('div')
#
# extract_text(node, text_re='返回顶部')
# print(extract_text(node, text_re='返回顶部'))
#
# print(iter_tree(node, text_re='返回顶部'))
