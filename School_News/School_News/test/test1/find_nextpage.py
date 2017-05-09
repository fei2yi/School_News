from selenium import webdriver
from scrapy.http import HtmlResponse

browser = webdriver.Chrome()

start_urls = [
'http://www.shenhuagroup.com.cn/shjtww/1382682123396/mtzx_tzgg.shtml',
'http://www.ctg.com.cn/sxjt/xwzx/ttxw/index.html',
'http://www.ctg.com.cn/sxjt/_300821/ldgh/index.html',
'http://www.ctg.com.cn/sxjt/_300821/xwdt/_301576/index.html',
'http://www.hunan.gov.cn/zw/jytabl/qgrddbjy/',
]
list = ['nea_gov_cn.NeaSpider',
        'hbj_nea_gov_cn.HbjNeaSpider',
        'dbj_nea_gov_cn.DbjNeaSpider',
        'xbj_nea_gov_cn.XbjNeaSpider',
        'hdj_nea_gov_cn.HdjNeaSpider',
        'hzj_nea_gov_cn.HzjNeaSpider',
        'nfj_nea_gov_cn.NfjNeaSpider',
        'sxb_nea_gov_cn.SxbNeaSpider',
        'sdb_nea_gov_cn.SdbNeaSpider',
        'gsb_nea_gov_cn.GsbNeaSpider',
        'xjb_nea_gov_cn.XjbNeaSpider',
        'zjb_nea_gov_cn.ZjbNeaSpider',
        'jsb_nea_gov_cn.JsbNeaSpider',
        'fjb_nea_gov_cn.FjbNeaSpider',
        'henb_nea_gov_cn.HenbNeaSpider',
        'hunb_nea_gov_cn.HunbNeaSpider',
        'scb_nea_gov_cn.ScbNeaSpider',
        'ynb_nea_gov_cn.YnbNeaSpider',
        'gzb_nea_gov_cn.GzbNeaSpider',
        'nyj_ahpc_gov_cn.NyjAhpcSpider',
        'lndp_gov_cn.LndpSpider',
        'jldrc_gov_cn.JldrcSpider',
        'hljdpc_gov_cn.HljdpcSpider',
        'shdrc_gov_cn.ShdrcSpider',
        'jsdpc_gov_cn.JsdpcSpider',
        'zjdpc_gov_cn.ZjdpcSpider',
        'ahpc_gov_cn.AhpcSpider',
        'jxdpc_gov_cn.JxdpcSpider',
        'fjdpc_gov_cn.FjdpcHdfzSpider',
        'fjdpc_gov_cn.FjdpcSpider',
        'sdfgw_gov_cn.SdfgwSpider',
        'gddrc_gov_cn.GddrcSpider',
        'gxdrc_gov_cn.GxdrcSpider',
        'hnfgw_gov_cn.HnfgwXxgkSpider',
        'hnfgw_gov_cn.HnfgwSpider',
        'hbfgw_gov_cn.HbfgwSpider',
        'hbfgw_gov_cn.HbfgwGkSpider',
        'hbfgw_gov_cn.HbfgwGovinfoSpider',
        'hndrc_gov_cn.HndrcSpider',
        'scdrc_gov_cn.ScdrcSpider',
        'cqdpc_gov_cn.CqdpcSpider',
        'yndpc_yn_gov_cn.YndpcYnSpider',
        'gzdpc_gov_cn.GzdpcSpider',
        'xxgk_gzdpc_gov_cn.XxgkGzdpcSpider',
        'xdrc_gov_cn.XdrcSpider',
        'qddpc_gov_cn.QddpcSpider',
        'web_shenyang_cn.WebShenyangAsseSpider',
        'web_shenyang_cn.WebShenyangSpider',
        'fgw_harbin_gov_cn.FgwHarbinSpider',
        'xadrc_gov_cn.XadrcSpider',
        'whdrc_gov_cn.WhdrcSpider',
        'gzplan_gov_cn.GzplanGzSpider',
        'gzplan_gov_cn.GzplanSpider',
        'njdpc_gov_cn.NjdpcSpider',
        'ccdrc_gov_cn.CcdrcSpider',
        'hzdpc_gov_cn.HzdpcSpider',
        'jndpc_gov_cn.JndpcSpider',
        'miit_gov_cn.MiitSpider',
        'bjeit_gov_cn.BjeitSpider',
        'bca_gov_cn.BcaSpider',
        'tjec_gov_cn.TjecSpider',
        'smetj_gov_cn.SmetjSpider',
        'tjca_gov_cn.TjcaSpider',
        'ii_gov_cn.IiSpider',
        'hbjg_gov_cn.HbjgSpider',
        'smejl_gov_cn.SmejlSpider',
        'jlca_gov_cn.JlcaSpider',
        'hljiic_gov_cn.HljiicSpider',
        'smehlj_gov_cn.SmehljSpider',
        'hlca_gov_cn.HlcaSpider',
        'sheitc_gov_cn.SheitcSpider',
        '1128_org.1128OrgSpider',
        'shca_gov_cn.ShcaSpider',
        'jseic_gov_cn.JseicSpider',
        'jseic_gov_cn.JseicXxgkSpider',
        'smejs_gov_cn.SmejsSpider',
        'bsdt_jsca_gov_cn.BsdtJscaSpider',
        'jsca_gov_cn.JscaSpider',
        'zjjxw_gov_cn.ZjjxwSpider',
        'zjjxw_gov_cn.ZjjxwColSpider',
        'zjsme_gov_cn.ZjsmeSpider',
        'zca_gov_cn.ZcaSpider',
        'aheic_gov_cn.AheicInfoSpider',
        'aheic_gov_cn.AheicSpider',
        'ahta_gov_cn.AhtaSpider',
        'fjetc_gov_cn.FjetcSpider',
        'fjca_gov_cn.FjcaSpider',
        'fjca_gov_cn.FjcaInfoSpider',
        'jxciit_gov_cn.JxciitSpider'
        ]  # for url in start_urls:
for index, url in enumerate(start_urls):
    res = browser.get(url)
    text = input()
    if text == 'a':
        pass
        # browser.quit()
        # try:
        #     next = browser.page_source
        #     # next = browser.find_element_by_xpath('//a[contains(text(),"下一页")]').get_attribute("value")
        #     # end = browser.page_source
        #     # .find_element_by_xpath('//a[contains(text(),"下一页")]/@href').extract_first()
        #     # .find_element_by_xpath('//a[contains(text(),"尾页")]/@href').extract_first()
        #     print(next)
        #     new_path_filename = r'C:\Users\yf\Desktop\abcqq\{}.txt'.format(list[index])
        #     f = open(new_path_filename, 'w', encoding='utf8')
        #     string = '{}'
        #     xml = string.format(next)
        #     f.write(xml)
        #     f.close()
        #     print('有')
        # except:
        #     i = i + 1
        #     print('木有', i)
#

# for index, url in enumerate(start_urls):
#     new_path_filename = r'C:\Users\yf\Desktop\abcqq\{}.txt'.format(list[index])
#     f = open(new_path_filename, 'r', encoding='utf8')
#     text = f.read()
#     if '>下一页' in text:
#         print(list[index],'yes')
#     elif '>下页' in text:
#         print(list[index],'yes')
#     else:
#         print('no')
#     f.close()
#     # print(index + 1, '有')
