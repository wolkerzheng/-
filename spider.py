#encoding=utf8

import  re
import urllib2
import urllib
import os
from bs4 import BeautifulSoup
import requests

class spider():
    def __init__(self):
        self.cookie = {
            'cookie': "SINAGLOBAL=6330698694441.539.1475299133020; wb_g_upvideo_2110388972=1; YF-V5-G0=3717816620d23c89a2402129ebf80935; YF-Ugrow-G0=ad83bc19c1269e709f753b172bddb094; SSOLoginState=1487766396; _s_tentry=login.sina.com.cn; Apache=9466487698800.918.1487766398101; ULV=1487766398116:26:4:3:9466487698800.918.1487766398101:1487750231370; YF-Page-G0=00acf392ca0910c1098d285f7eb74a11; wvr=6; SCF=AurFLudiFxxlqSVrZqZfYFxe5Ltzg2RLyf9mHjIunmUm1IdbWMikokfZWK2jVdxNJtV-ZiBLlJG25-GvdWisoX8.; SUB=_2A251tIHZDeRxGeRP6lIS-CbFzD6IHXVWw_QRrDV8PUNbmtBeLVfVkW8i7jGLhn6CDNGpNnOM0wK_ytOOcg..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF.WxwwDJAGGXfuh2UCYMki5JpX5KMhUgL.FozpeK501hn4S0z2dJLoI0YLxKqL1hnL1K2LxKnLBo-LBoMLxKBLB.2L1hqLxKBLBonLB-2LxKqL1KqLBo5LxK-L1K5L12BLxK-LB-BL1KMt; SUHB=0G0ff2NgL347wv; ALF=1519527177; wb_publish_fist100_2110388972=1; UOR=www.panda.tv,widget.weibo.com,www.baidu.com"}

        self.list = []
        self.result = None

    def getText(self):
        # pagenum = self.getPageNum(user_id)

        url = 'http://weibo.com/p/10012019609/review'
        response = requests.get(url, cookies=self.cookie).content
        print response
        soup = BeautifulSoup(response, 'lxml')
        # print soup
        contents = soup.find_all('div', class_='WB_empty')
            # selector=etree.HTML(response)
            # contents=selector.xpath('//span[@class="mp"]')
        print contents
        for content in contents:
            text = ''
            texts = content.stripped_strings
            # texts=content.xpath('string(.)')
            for text_ in texts:  # 有些，一条微博内容分几部分，先将它合并成一个字符串
                text = text + ',' + text_
            # text=','.join(texts)
            self.list.append(text)

        for text in self.list:  # 处理输出格式，比如每条微博前面加序号
            print text

            text = text + '\r\n'
            self.result = self.result + text

        return self.result



    def Start(self):
        print u"爬虫准备就绪……"
        self.getText()
        print u"爬取完毕"


x = spider()
x.Start()
