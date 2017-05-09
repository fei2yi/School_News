from selenium import webdriver
from scrapy.http import HtmlResponse
import time

browser = webdriver.PhantomJS()
# browser = webdriver.Chrome()

# start_urls = [
#     #湖南政府的初步分组，未完成。
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/hjsf/hjbl_55961/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/hjsf/sfzbl_55966/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/hjsf/ggrysfqr/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/hjsf/jzzbl_55974/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/jyfw/xqjy/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/jyfw/xxjy/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/jyfw/czjy/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/jyfw/gzjy/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/jyfw/gdjy/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/jyfw/zyjy/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/jyfw/jxjy/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/jyfw/tsjy/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/jyfw/dwjlylx/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/jyfw/jyqzyzz/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/jyfw_55182/zyjn/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/jyfw_55182/jyaz/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/jyfw_55182/zzcy/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/jyfw_55182/ldqy/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/sbfw/shbx/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/sbfw/shfl/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/sbfw/shjz/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/zffw/bzxzf_56201/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/zffw/spf/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/zffw/gjj/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/hysy/hy/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/hysy/sy/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/hysy/sy_56287/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/yljk/kbjy/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/yljk/jkfw/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/yljk/yljz/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/jtfw/jtcx/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/jtfw/jdcfw/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/jtfw/jsrfw/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/cjrj/hzbl_56378/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/cjrj/txzbl/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/cjrj/qzbl/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/zyzg/ylwsl/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/zyzg/sflsl/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/zyzg/jtlyl/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/zyzg/mywll/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/zyzg/jjjrl/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/zyzg/gcjsl/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/zyzg/tzsbzyl/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/zyzg/xwjzl/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/gysy/szgyss/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/gysy/wtxx/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/gysy/ydlh/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/snfw/zcfgyjd_56488/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/snfw/fwzn_56489/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/snfw/cjwtjd_56490/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/zhqt_55192/bzfw/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/zhqt_55192/byfw/ ',
#     'http://www.hunan.gov.cn/fw/grfw/ztlb/zhqt_55192/mzzj_56500/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/cs/syyt_56509/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/cs/sye_d_t_56514/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/cs/syjlfz_56519/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/sx/xqjy_56523/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/sx/xxjy_56528/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/sx/czjy_56533/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/sx/gzjy_56538/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/sx/gdjy_56544/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/sx/zyjy_56550/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/sx/jxjy_56556/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/sx/tsjy_56563/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/sx/dwjlylx_56568/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/sx/jyqzyzz_56573/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/gz/zyjn_56596/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/gz/jyaz_56606/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/gz/zzcy_56623/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/gz/zyzg_56627/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/mf/jjsyf_56683/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/mf/spf_56687/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/jh/zcfgyjd_56703/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/jh/bszn_56704/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/jh/clxz_56705/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/jh/cjwtjd_56706/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/yl/kbjy_56707/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/yl/jkfw_56716/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/yl/ylbx_56739/ ',
#     'http://www.hunan.gov.cn/fw/grfw/rssj/yl/lnrfl_56744/ ',
#     'http://www.hunan.gov.cn/fw/grfw/tsqt/et/xqjy_56749/ ',
#     'http://www.hunan.gov.cn/fw/grfw/tsqt/et/xxjy_56754/ ',
#     'http://www.hunan.gov.cn/fw/grfw/tsqt/et/kbjy_56759/ ',
#     'http://www.hunan.gov.cn/fw/grfw/tsqt/et/etfl_56768/ ',
#     'http://www.hunan.gov.cn/fw/grfw/tsqt/fn/jh_56773/ ',
#     'http://www.hunan.gov.cn/fw/grfw/tsqt/fn/sy_56778/ ',
#     'http://www.hunan.gov.cn/fw/grfw/tsqt/lnr/kbjy_56793/ ',
#     'http://www.hunan.gov.cn/fw/grfw/tsqt/lnr/jkfw_56802/ ',
#     'http://www.hunan.gov.cn/fw/grfw/tsqt/lnr/ylbx_56825/ ',
#     'http://www.hunan.gov.cn/fw/grfw/tsqt/lnr/lnrfl_56830/ ',
#     'http://www.hunan.gov.cn/fw/grfw/tsqt/cjr/zcfgyjd_56835/ ',
#     'http://www.hunan.gov.cn/fw/grfw/tsqt/cjr/fwzn_56836/ ',
#     'http://www.hunan.gov.cn/fw/grfw/tsqt/cjr/clxz_56837/ ',
#     'http://www.hunan.gov.cn/fw/grfw/tsqt/cjr/cjrfwjg_56838/ ',
#     'http://www.hunan.gov.cn/fw/grfw/tsqt/cjr/cjwtjd_56839/ ',
#     'http://www.hunan.gov.cn/fw/grfw/tsqt/wgr/zcfgyjd_56840/ ',
#     'http://www.hunan.gov.cn/fw/grfw/tsqt/wgr/fwzn_56841/ ',
#     'http://www.hunan.gov.cn/fw/grfw/tsqt/wgr/clxz_56842/ ',
#     'http://www.hunan.gov.cn/fw/grfw/tsqt/wgr/cjwtjd_56843/ ',
#     'http://www.hunan.gov.cn/fw/frfw/slbg/',
#     'http://www.hunan.gov.cn/fw/frfw/zyzb/',
#     'http://www.hunan.gov.cn/fw/frfw/zzrz/',
#     'http://www.hunan.gov.cn/fw/frfw/tzlx/',
#     'http://www.hunan.gov.cn/fw/frfw/gcjs_55171/',
#     'http://www.hunan.gov.cn/fw/frfw/jyns/',
#     'http://www.hunan.gov.cn/fw/frfw/aqfh/',
#     'http://www.hunan.gov.cn/fw/frfw/zljd/',
#     'http://www.hunan.gov.cn/fw/frfw/swsw/',
#     'http://www.hunan.gov.cn/fw/frfw/pczx/',
#     'http://www.hunan.gov.cn/fw/frfw/zhqt/',
#
# ]
start_urls = [
'http___fgw.xjbt.gov.cn_bt_jrbt_jjsh_shfz_.txt',
'http___fgw.xjbt.gov.cn_gk_tzgg_.txt',
'http___fgw.xjbt.gov.cn_xw_bmdt_.txt',
'http___fgw.xjbt.gov.cn_zt_ddqzlxjysjhd_pljd_.txt',
'http___info.hebei.gov.cn_eportal_ui_.txt',
'http___www.ah.gov.cn_tmp_Nav_banshilanmu.shtml_PS_ID=1&S_ID=11.txt',
'http___www.ah.gov.cn_UserData_SortHtml_1_26234719403.html.txt',
'http___www.ah.gov.cn_UserData_SortHtml_1_37683846130.html.txt',
'http___www.ah.gov.cn_UserData_SortHtml_1_42877632143.html.txt',
'http___www.china-cdt.com_dtwz__indexAction.ndo_action=showNewsInYearList&t=index_news&s=news_dtxw.txt',
'http___www.hebei.gov.cn_hebei_11937442_10761139_index.html.txt',
'http___www.jl.gov.cn_ggzyjy_ggzyjy_.txt',
'http___www.jl.gov.cn_zw_77306_.txt',
'http___www.jl.gov.cn_zw_77306_wj_.txt',
'http___www.jl.gov.cn_zw_77306_xxgk_jdjcdc_.txt',
'http___www.ln.gov.cn_qmzx_0.txt',
'http___www.ln.gov.cn_zfxx_.txt',
'http___www.ln.gov.cn_zfxx_qsgd_ass_.txt',
'http___www.ln.gov.cn_zfxx_qsgd_ass_1_.txt',
'http___www.ln.gov.cn_zfxx_qsgd_ass_1_1_.txt',
'http___www.ln.gov.cn_zfxx_qsgd_ass_2_.txt',
'http___www.ln.gov.cn_zfxx_qsgd_ass_2_1_.txt',
'http___www.ln.gov.cn_zfxx_qsgd_ass_2_1_1_.txt',
'http___www.ln.gov.cn_zfxx_qsgd_ass_2_1_1_1_.txt',
'http___www.ln.gov.cn_zfxx_qsgd_ass_2_1_1_1_1_.txt',
'http___www.ln.gov.cn_zfxx_qsgd_ass_2_1_1_1_1_1_.txt',
'http___www.ln.gov.cn_zfxx_qsgd_dls_.txt',
'http___www.ln.gov.cn_zfxx_qsgd_fxs_.txt',
'http___www.ln.gov.cn_zfxx_qsgd_hld_.txt',
'http___www.ln.gov.cn_zfxx_qsgd_yks_.txt',
'http___www.ln.gov.cn_zfxx_qsgd_yks_1_.txt',
'http___www.nmg.gov.cn_banshi_.txt',
'http___www.nmg.gov.cn_fabu_.txt',
'http___www.nmg.gov.cn_fabu_xwdt_ms_.txt',
'http___www.nmg.gov.cn_wz_.txt',
'http___www.nmg.gov.cn_zfsj_.txt',
'http___www.nmg.gov.cn_zzqzf_.txt',
'http___www.shanxi.gov.cn_gzsj_.txt',
'http___www.shanxi.gov.cn_hdjl_.txt',
'http___www.shanxi.gov.cn_xxgk_.txt',
'http___www.shanxigov.cn_xxgk_xwzx_.txt',
'http___xxgk.hainan.gov.cn_hi_szfzw.html_txt=24880_25181_25184_list.htm.txt',
'http___zhengwu.beijing.gov.cn_.txt',
]

zifu = ['/', ':', '*', '?', '"', '<', '> ', '|']

for index, url in enumerate(start_urls):
    file_name = start_urls[index]
    for i in zifu:
        if i in file_name:
            file_name = file_name.replace(i, '_')
    browser.get(url)
    # //a[contains(text(), "点击进入")]//a
    # tip = browser.find_elements_by_xpath('//div[@class="fl"]//a')
    # for i in tip:
    #     time.sleep(2)
    #     print(i.text)
    #     # i.click()

    # print(groups)
    groups = browser.find_elements_by_xpath('//table[@class="ipRtbl_year"]//td')
    new_path_filename = r'C:\Users\yf\Desktop\abc\{}.txt'.format(file_name)

    for index, group in enumerate(groups):
        href = group.get_attribute("onclick")
        text = group.find_element_by_xpath('.').text
        print(href, text)
        time.sleep(1)
        f = open(new_path_filename, 'a', encoding='utf8')
        string = '{},{}'
        xml = string.format(href, text)
        f.write(xml)
        f.close()
    print('有', index + 1)
# #


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
