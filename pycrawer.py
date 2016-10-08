#encoding=utf-8
import urllib
import urllib2
import cookielib
import sys
from bs4 import BeautifulSoup

# #创建cookies容器
# cj = cookielib.CookieJar()
# #创建一个opener
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# #给urllib2安装opener
# urllib2.install_opener(opener)
# #使用带有cookies的urllib2访问网页
# response =  urllib2.urlopen("http://www.baidu.com/")
reload(sys)
sys.setdefaultencoding('utf-8')
url = "http://www.zhihu.com/explore"
# page = (raw_input())
url = 'http://www.qiushibaike.com/hot/page/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
with open('output.txt','w') as f:
    for i in xrange(1,11):
        url = url + str(i)
        try:
            req = urllib2.Request(url,headers = headers)
            response = urllib2.urlopen(req)
            html_doc = (response.read())
            soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
            links =  soup.find_all("div",class_="content")
            for line in links:
                cont = line.get_text()
                f.write(cont)
                f.flush()
                print line.name,cont
            # print response.read()
        except urllib2.URLError,e:
            if hasattr(e,'code'):
                print e.code
            if hasattr(e,'reason'):
                print e.reason

# user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) ' \
#              'AppleWebKit/537.36 (KHTML, like Gecko) ' \
#              'Chrome/52.0.2743.116 Safari/537.36'
# values={
#     'Accept-Language':'zh-CN,zh;q=0.8',
#     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Accept-Encoding':'gzip,deflate,sdch,br',
#     'Cookie':'q_c1=8c97b328438d41e3a013455d93dd58b0|1474251558000|1474251558000; l_cap_id=Njk2MmE1OGRjNzVjNGFjOGI1YzRiNzAzZThlZmQxMjc=|1474251558|d0f22d81273ca06457b92279a81767a32f13e23b; cap_id=MWM1MGM1ZTAwODllNDIxYWFmOWEyMDk4OWQwZjhiMjk=|1474251558|97769df2f2fd5cad875d7d825cda3279c25eb459; n_c=1; d_c0=AGDAEBAjkAqPTkqXUjJ-pBNYE-KToG8trls=|1474251559; _zap=eb1b7e11-7d46-456a-af4a-3637f04b178d; __utma=51854390.142818869.1474251591.1474251591.1474251591.1; __utmb=51854390.4.10.1474251591; __utmc=51854390; __utmz=51854390.1474251591.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|3=entry_date=20160919=1; __utmt=1; _xsrf=20e2397aabdfc686ee0bcb118c79dd0a; _za=094b2493-9f8a-4d61-b2dd-258aaa8a59a6',
#     'Upgrade-Insecure-Request':'1'
# }
# headers = {'User-Agent':user_agent}
# data = urllib.urlencode(values)
# req = urllib2.Request(url,data,headers)
# response = urllib2.urlopen(req)
# html = response.read()
# soup = BeautifulSoup(html)
# print soup.title


