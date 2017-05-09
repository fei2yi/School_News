# fujian_gov_cn.FujianPicSpider  未找到public_time ,public_time在换行的字符串中。    terminal的测试 失败，spider run成功。无用删掉。
# fujian_gov_cn.FujianYjglSpider  来源 未获取到，原因不详。  内容页面的source为JavaScript生成，而打开内容页面的方式默认为普通open。
# nmgjxw_gov_cn.NmgjxwSpider  的list 新闻链接为空，不能跳转，网页有问题。
# http://hdj.nea.gov.cn    来源未匹配成功,内容未成功，分页未成功
# http://hzj.nea.gov.cn  的内容页面为动态加载
# http://nfj.nea.gov.cn  无法访问
# http://www.hljdpc.gov.cn   无法访问，path 未匹配。
# www.yndpc.yn.gov.cn   无法访问
# ccdrc_gov_cn.CcdrcSpider  未完成
# http://www.hbjg.gov.cn    无法访问
# gd_gov_cn.GdCzzSpider  下，打开文章链接各种情况，不统一。

# 问题：
#  start_url的异步请求问题，伴随clickaction()发生。
#  post()请求问题。
#  用back()解决返回之前请求的列表。
#  'whdrc_gov_cn.WhdrcSpider',最后一页存在死循环问题。
#  '通过hash()的字符串的对比，解决问题。

# iframe问题：
#   hzj_nea_gov_cn.HzjNeaSpider  content 在iframe内，未获取到。
#  'scdrc_gov_cn.ScdrcSpider',   列表在iframe里。iframe问题通过手动找iframe的URL。
#  还存在部分要获取内容在iframe里，部分在之外。

# source 问题
#  'aheic_gov_cn.AheicSpider',   # source未获取到。是字符编码的原因 ，未获取到，已解决。

# 下一页问题：
#  'sdb_nea_gov_cn.SdbNeaSpider',       未通过  http://sdb.nea.gov.cn/new/list.asp?boardid=18  此页面无下一页尾页，而有的页面有。
# 由于URL有特征，采用数字增加的方式，页面上是有总页数的，加获取总页数的方法。
#  http://jsb.nea.gov.cn/info/community/101-p6.html     没有下一页 ，尾页。分页未写。
# 同上
#  'jxdpc_gov_cn.JxdpcSpider',       # 未通过,只走了两页，第二页的时候，存在下一页按钮消失现象。
# 此现象演示时未出现。
#  'fjb_nea_gov_cn.FjbNeaSpider',     在分页中间的时候，遇到异常scrapy.exceptions.NotSupported: Unsupported URL scheme 'javascript': no handler available for that scheme
# item的xpath配置为style产生的异常 ，换 xpath配置，问题解决。

# 其他：
#  'ii_gov_cn.IiSpider',     异常：element not visible
# 有两个下一页元素，第一个是隐藏元素。
#  'hnfgw_gov_cn.HnfgwXxgkSpider',   voice元素看得见，程序找不到。
# 等待几秒，就可以获取到。
#  文章列表中的li有的中没有URL，会报keyerror[url]错误，可以采用让此异常通过的方法。
# 仍旧采用xpath解决。
#  http://www.china-cdt.com/dtwz//indexAction.ndo?action=showNewsInYearList&t=index_news&s=news_dtxw&y=2017  大唐集团的文章href为Javascript生成。
# 获取href的字符串，用xpath取出url.
# 'zca_gov_cn.ZcaSpider',
# a元素属性href异常（第三个列表）
# 'xxgk_hainan_gov_cn.XxgkHiSpider',
# 下一页元素不可见
# 'sydrc_gov_cn.SydrcSpider',
# 响应时间过长
# 'web_shenyang_cn.WebShenyangJjSpider',
# 响应时间过长
# 'web_shenyang_cn.WebShenyangZcSpider',
# 响应时间过长
# 'smejl_gov_cn.SmejlSpider',
# 无下一页
# 'sheitc_gov_cn.SheitcSpider',
# click点击有问题
# 'sc_gov_cn.ScSpider',
# click分页 未点击
# 'jiangxi_gov_cn.JiangxiSpider',
# source未获取
# 'hljiic_gov_cn.HljiicSpider',
# 点击存在不一定性，不能它是否点完，而且存在点击到中间请求超时现象，页面加载失败现象。
# 'hbjg_gov_cn.HbjgSpider',
# 被拒绝。
# 'fgw_xjbt_gov_cn.FgwZtSpider',
# 存在最后一页死循环请求，请求方式为浏览器打开方式。需用hash比对。
# 'ecp_cgnpc_com_cn.ecpSpider',
# 下一页隔页点击，而实际不能点击。
# 'fgw_xjbt_gov_cn.FgwGkSpider',
# 存在最后一页死循环请求，请求方式为浏览器打开方式。需用hash比对。
# 'fgw_xjbt_gov_cn.FgwXwSpider',
# 存在最后一页死循环请求，请求方式为浏览器打开方式。需用hash比对。
# 'chng_com_cn.Chng8Spider',
# 点到了下一页，但只获取了第一页数据。
# 'cq_gov_cn.CqInfoSpider',
# 点到了下一页，但只获取了第一页数据。
# 'chng_com_cn.Chng6Spider',
# 点到了下一页，但只获取了第一页数据。
# 'chng_com_cn.Chng4Spider',
# source未获取到。
# 'chng_com_cn.Chng1Spider',
# 点击操作中途停止现象。
# 'cgdc_com_cn.CgdcSpider',
# 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。
# 'cgnpc_com_cn.CgnpcSpider',
# 点击操作中途停止现象。
# 'chd_com_cn.Chd2Spider',
# 点击操作中途停止现象。
#twisted.internet.error.ReactorNotRestartable