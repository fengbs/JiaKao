import urllib.request
import urllib.parse
from bs4 import *
from urllib.parse import urljoin
import sqlite3 
#从立秋驾培网站中爬下地方考题
class crawler:
    def crawl(self):#题目编号从1864 到 2062
        UrlStr = 'http://hebei.iabe.cn/newsubjects/Test-Analysis-'
        outputFile = open('hebeijiakao.txt','w')
        for i in range(1864,2063):
            newURL = UrlStr + str(i)+'.html'
            try:
                 c = urllib.request.urlopen(newURL)
            except:
                print('could not open page %s' % newURL)
                continue
            soup = BeautifulSoup(c.read(),"html.parser")
            links = soup('div')
            outputFile.write(str(i-1863)+'.')
            for link in links:
                if ('class' in dict(link.attrs)):
                    if(link['class'][0] == 'topic_title'):
                        outputFile.write(link.get_text().strip())
                        outputFile.write('\n\n')
                    if(link['class'][0] == 'topic_option'):
                        outputFile.write(link.get_text().strip())
                        outputFile.write('\n\n')
                    if(link['class'][0] == 'trueAnswer'):
                        outputFile.write(link.get_text().strip())
                        outputFile.write('\n\n')
                    if(link['class'][0] == 'bestAnswer_content'):
                        outputFile.write('答案分析： %s\n' % link.get_text().strip())
            outputFile.write('-----------------------------------------------------------------------\n')
        outputFile.close()
                

    #处理post表单请求部分
    def sol_form(self,pages,num = 0):
        params = {'__EVENTTARGET':'ctl00$ContentPlaceHolder1$pager','__EVENTARGUMENT':1}
        postdata = urllib.parse.urlencode(params)
        postdata = postdata.encode('utf-8')
        myheaders = {"Content-Type": "application/x-www-form-urlencoded"}
        r = urllib.request.Request(pages[0],data = postdata,headers = myheaders)
        html = urllib.request.urlopen(r)
        print(type(html))
        print( html.read().decode('gb2312'))
        return html.read().decode('gb2312')
        
        
        
    
    
