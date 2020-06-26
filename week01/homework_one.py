# 使用BeautifulSoup解析网页

import requests
from bs4 import BeautifulSoup as bs
# bs4是第三方库需要使用pip命令安装
import requests
import lxml.etree
import re
import pandas as pd

header={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'__mta=53834519.1583065701340.1583108060211.1583108060676.20; uuid_n_v=v1; uuid=22053C605BB811EA9F0985C24ED856C3328A984601984D769ABA5F0CB37F9375; _csrf=ea175c7bf99c2857a14ab1f681c5b2ecda89ad7d289d75398ec75e3be3fced4e; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1583065701; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=17096119979c8-002e7da7eaa60d-4313f6b-144000-1709611997ac8; mojo-uuid=dd0ebe64e78f7063615ea02b6a1e0aea; __mta=53834519.1583065701340.1583065822531.1583065825533.7; _lxsdk=22053C605BB811EA9F0985C24ED856C3328A984601984D769ABA5F0CB37F9375; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1583108061; _lxsdk_s=17098f889a5-f18-5b8-a84%7C%7C2',
        'Host':'maoyan.com',
        'Sec-Fetch-Dest':'document',
        'Sec-Fetch-Mode':'navigate',
        'Sec-Fetch-Site':'none',
        'Sec-Fetch-User':'?1',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
    }

myurl = 'https://maoyan.com/board/4'

response = requests.get(myurl,headers=header)
response.encoding ='utf-8'
bs_info = bs(response.text, 'html.parser')


# Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
myList=[]
for tags in bs_info.find_all('div', attrs={'class': 'board-item-content'}):
    for atag in tags.find_all('a'):
        #print(atag.get('href'))
        urls ='https://maoyan.com'+str(atag.get('href'))
        #print(urls)
        # 获取所有链接

        response1 = requests.get(urls, headers=header)
        bs_info1 = bs(response1.text, 'html.parser')
        kid = bs_info1.find_all('a', attrs={'class':'text-link'})
        movietype = re.findall(u"[\u4e00-\u9fa5]+",str(kid))                   
        # 电影类型
        #print(movietype)
        
        movienames=atag.get('title')
        #print(movienames)
        # 获取电影名字
    releasetimes= tags.find('p', attrs={'class': 'releasetime'},).text    
    #print(releasetimes)
        # 获取电影上映时间
    for btag in tags.find_all('div', attrs={'class':'movie-item-number score-num'}):
        #print(btag.find('i', ).text)
        #print(btag.find('i',attrs={'class': 'fraction'}, ).text)
        sore = str(btag.find('i', ).text)+str(btag.find('i',attrs={'class': 'fraction'}, ).text)
        #print(sore)
    myList.append([urls, movienames, releasetimes, sore, movietype])


movie1 = pd.DataFrame(data = myList)

# windows需要使用gbk字符集   
movie1.to_csv('./movie2.csv', encoding='gbk', index=False, header=False)


