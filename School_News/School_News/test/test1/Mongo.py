from pymongo import MongoClient

client = MongoClient('192.168.0.174', 27017)
db_name = 'telespy'
db = client[db_name]


def find():
    for index, spider_name in enumerate([
        "nyj_ahpc_gov_cn.AhnyjSpider",  # 安徽省能源局1-1
        "nyj_ahpc_gov_cn.DlcSpider",  # 安徽省能源局1-2
        "dbj_nea_gov_cn.DbjNeaSpider",  # 东北能源局1-3
        "gzcoal_gov_cn.GzcoalSpider",  # 贵州省能源局1-4
        "nea_gov_cn.NeaSpider",  # 国家能源局1-5
        "hbj_nea_gov_cn.HbjNeaSpider",  # 华北能源局1-6
        "hdj_nea_gov_cn.HdjNeaSpider",  # 华东能源局1-7
        "hzj_nea_gov_cn.HzjNeaSpider",  # 华中能源局1-8
        "nyj_jl_gov_cn.Nyj_jlSpider",  # 吉林省能源局1-9
        "nyj_jxdpc_gov_cn.NyjjxdpcSpider",  # 江西省能源局1-10
        "nfj_nea_gov_cn.NfjNeaSpider",  # 南方能源局1-11
        "sxsnyj_gov_cn.SxsnyjSpider",  # 陕西省能源局1-12
        "xbj_nea_gov_cn.XbjNeaSpider",  # 西北能源局1-13
        "fjb_nea_gov_cn.FjbNeaSpider",  # 福建能监办1-14
        "gsb_nea_gov_cn.GsbNeaSpider",  # 甘肃能监办1-15
        "gzb_nea_gov_cn.GzbNeaSpider",  # 贵州能监办1-16
        "henb_nea_gov_cn.HenbNeaSpider",  # 河南能监办1-17
        "hunb_nea_gov_cn.HunbNeaSpider",  # 湖南能监办1-18
        "jsb_nea_gov_cn.JsbNeaSpider",  # 江苏能监办1-19
        "sdb_nea_gov_cn.SdbNeaSpider",  # 山东能监办1-20
        "sxb_nea_gov_cn.SxbNeaSpider",  # 山西能监办1-21
        "scb_nea_gov_cn.ScbNeaSpider",  # 四川能监办1-22
        "xjb_nea_gov_cn.XjbNeaSpider",  # 新疆能监办1-23
        "ynb_nea_gov_cn.YnbNeaSpider",  # 云南能监办1-24
        "zjb_nea_gov_cn.ZjbNeaSpider",  # 浙江能监办1-25
        "aheic_gov_cn.AheicInfoSpider",  # 安徽经信委1-26
        "aheic_gov_cn.AheicSpider",  # 安徽经信委1-27
        "bjeit_gov_cn.BjeitSpider",  # 北京经信委1-28
        "fjetc_gov_cn.FjetcSpider",  # 福建经信委1-29
        "gdei_gov_cn.DsdtSpider",  # 广东经信委1-30
        "gdei_gov_cn.SzywSpider",  # 广东经信委1-31
        "gdei_gov_cn.XzzsSpider",  # 广东经信委1-32
        "gzjxw_gov_cn.GfxwjSpider",  # 贵州经信委1-33
        "hbeitc_gov_cn.Hbeitc_csSpider",  # 湖北经信委1-34
        "hbeitc_gov_cn.Hbeitc_homeSpider",  # 湖北经信委1-35
        "hbeitc_gov_cn.Hbeitc_xxgkSpider",  # 湖北经信委1-36
        "hnjxw_gov_cn.JxywSpider",  # 湖南经信委1-37
        "hnjxw_gov_cn.QzqdSpider",  # 湖南经信委1-38
        "hnjxw_gov_cn.WjtzSpider",  # 湖南经信委1-39
        "jseic_gov_cn.JseicSpider",  # 江苏经信委1-40
        "jseic_gov_cn.JseicXxgkSpider",  # 江苏经信委1-41
        "lneic_gov_cn.GzdtSpider",  # 辽宁经信委1-42
        "lneic_gov_cn.ZdgzSpider",  # 辽宁经信委1-43
        "nmgjxw_gov_cn.NmgjxwSpider",  # 内蒙古经信委1-44
        "nxetc_gov_cn.GwywjSpider",  # 宁夏经信委1-45
        "qhec_gov_cn.XzspSpider",  # 青海经信委1-46
        "sdeic_gov_cn.SdeicSpider",  # 山东经信委1-47
        "sheitc_gov_cn.SheitcSpider",  # 上海经信委1-48
        "scjm_gov_cn.GzdtSpider",  # 四川经信委1-49
        "scjm_gov_cn.TpxwSpider",  # 四川经信委1-50
        "xjeic_gov_cn.GzdtSpider",  # 新疆经信委1-51
        "zjjxw_gov_cn.ZjjxwColSpider",  # 浙江经信委1-52
        "zjjxw_gov_cn.ZjjxwSpider",  # 浙江经信委1-53
        "wjj_cq_gov_cn.Gygkspider",  # 重庆经信委1-54
    ]):
        collection_useraction = db['clues'].find({"spider_name": "{}".format(spider_name)}).count()
        print(index + 1, spider_name, "线索数：", collection_useraction, '-------------------------')
        # if collection_useraction != 0:
        #     group = db['clues'].find({"spider_name": "{}".format(spider_name)})
        #     a = set()
        #     for i in group:
        #         a.add(i['group'])
        #     sum = {}
        #     #
        #     # for index, group in enumerate(a):
        #     #     if group:
        #     #         sum[index] = sum[index] + 1
        #     #         {}[i['group']] = {}[i['group']] + 1
        #     #
        #     # print(spider_name, "线索数：", collection_useraction, '列表名', )


def delete():
    for index, spider_name in enumerate([
        # "nyj_ahpc_gov_cn.AhnyjSpider",  # 安徽省能源局1-1
        # "nyj_ahpc_gov_cn.DlcSpider",  # 安徽省能源局1-2
        # "dbj_nea_gov_cn.DbjNeaSpider",  # 东北能源局1-3
        # "gzcoal_gov_cn.GzcoalSpider",  # 贵州省能源局1-4
        # "nea_gov_cn.NeaSpider",  # 国家能源局1-5
        # "hbj_nea_gov_cn.HbjNeaSpider",  # 华北能源局1-6
        # "hdj_nea_gov_cn.HdjNeaSpider",  # 华东能源局1-7
        # "hzj_nea_gov_cn.HzjNeaSpider",  # 华中能源局1-8
        # "nyj_jl_gov_cn.Nyj_jlSpider",  # 吉林省能源局1-9
        # "nyj_jxdpc_gov_cn.NyjjxdpcSpider",  # 江西省能源局1-10
        # "nfj_nea_gov_cn.NfjNeaSpider",  # 南方能源局1-11
        # "sxsnyj_gov_cn.SxsnyjSpider",  # 陕西省能源局1-12
        # "xbj_nea_gov_cn.XbjNeaSpider",  # 西北能源局1-13
        # "fjb_nea_gov_cn.FjbNeaSpider",  # 福建能监办1-14
        # "gsb_nea_gov_cn.GsbNeaSpider",  # 甘肃能监办1-15
        # "gzb_nea_gov_cn.GzbNeaSpider",  # 贵州能监办1-16
        # "henb_nea_gov_cn.HenbNeaSpider",  # 河南能监办1-17
        # "hunb_nea_gov_cn.HunbNeaSpider",  # 湖南能监办1-18
        # "jsb_nea_gov_cn.JsbNeaSpider",  # 江苏能监办1-19
        # "sdb_nea_gov_cn.SdbNeaSpider",  # 山东能监办1-20
        # "sxb_nea_gov_cn.SxbNeaSpider",  # 山西能监办1-21
        # "scb_nea_gov_cn.ScbNeaSpider",  # 四川能监办1-22
        # "xjb_nea_gov_cn.XjbNeaSpider",  # 新疆能监办1-23
        # "ynb_nea_gov_cn.YnbNeaSpider",  # 云南能监办1-24
        # "zjb_nea_gov_cn.ZjbNeaSpider",  # 浙江能监办1-25
        # "aheic_gov_cn.AheicInfoSpider",  # 安徽经信委1-26
        # "aheic_gov_cn.AheicSpider",  # 安徽经信委1-27
        # "bjeit_gov_cn.BjeitSpider",  # 北京经信委1-28
        # "fjetc_gov_cn.FjetcSpider",  # 福建经信委1-29
        # "gdei_gov_cn.DsdtSpider",  # 广东经信委1-30
        # "gdei_gov_cn.SzywSpider",  # 广东经信委1-31
        # "gdei_gov_cn.XzzsSpider",  # 广东经信委1-32
        # "gzjxw_gov_cn.GfxwjSpider",  # 贵州经信委1-33
        # "hbeitc_gov_cn.Hbeitc_csSpider",  # 湖北经信委1-34
        # "hbeitc_gov_cn.Hbeitc_homeSpider",  # 湖北经信委1-35
        # "hbeitc_gov_cn.Hbeitc_xxgkSpider",  # 湖北经信委1-36
        # "hnjxw_gov_cn.JxywSpider",  # 湖南经信委1-37
        # "hnjxw_gov_cn.QzqdSpider",  # 湖南经信委1-38
        # "hnjxw_gov_cn.WjtzSpider",  # 湖南经信委1-39
        # "jseic_gov_cn.JseicSpider",  # 江苏经信委1-40
        # "jseic_gov_cn.JseicXxgkSpider",  # 江苏经信委1-41
        # "lneic_gov_cn.GzdtSpider",  # 辽宁经信委1-42
        # "lneic_gov_cn.ZdgzSpider",  # 辽宁经信委1-43
        # "nmgjxw_gov_cn.NmgjxwSpider",  # 内蒙古经信委1-44
        # "nxetc_gov_cn.GwywjSpider",  # 宁夏经信委1-45
        # "qhec_gov_cn.XzspSpider",  # 青海经信委1-46
        # "sdeic_gov_cn.SdeicSpider",  # 山东经信委1-47
        # "sheitc_gov_cn.SheitcSpider",  # 上海经信委1-48
        # "scjm_gov_cn.GzdtSpider",  # 四川经信委1-49
        # "scjm_gov_cn.TpxwSpider",  # 四川经信委1-50
        # "xjeic_gov_cn.GzdtSpider",  # 新疆经信委1-51
        # "zjjxw_gov_cn.ZjjxwColSpider",  # 浙江经信委1-52
        # "zjjxw_gov_cn.ZjjxwSpider",  # 浙江经信委1-53
        # "wjj_cq_gov_cn.Gygkspider",  # 重庆经信委1-54
    ]):
        # db['clues'].remove({"spider_name": "{}".format(spider_name)})
        print(spider_name, "删除成功")


find()
# delete()
