import jiaxiao
pages = ['http://hebei.iabe.cn/public/Test_List.aspx?TiMuXiaoLeiLiuShuiHao=9','http://hebei.iabe.cn/public/Test_List.aspx?TiMuXiaoLeiLiuShuiHao=9']
jx = jiaxiao.crawler()
#jx.sol_form(pages)
jx.crawl()
