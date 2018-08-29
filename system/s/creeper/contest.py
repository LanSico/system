import urllib
import re
import http.cookiejar
import MySQLdb
import time

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

db = MySQLdb.connect("localhost", "root", "djj0209.", "cs_sys", charset='utf8')
cursor=db.cursor()

#while(True):
page=1
res=urllib.request.urlopen("https://www.saikr.com/vs/0/0/0?page="+str(page))
cont=res.read().decode("utf-8")
rc = re.compile(r'<a href="(.*?)" target="_blank" title=".*?" class="link">')
req = rc.findall(cont)
for i in req:
    res=urllib.request.urlopen(i)
    cont=res.read().decode("utf-8")
    rc2 = re.compile(r'<h1 class="event-title">(.*?)</h1>')
    req2 = rc2.findall(cont)
    #for t in req2:
    #    print(t)       #标题
    rc2 = re.compile(r'<span class="title-desc">\s*(.*?)\s*</span>')
    req2 = rc2.findall(cont)
    #for t in req2:
    #    print(t)        #浏览量 类型 费用 级别 参赛对象 "关注后，有更新时会通知您" 关注人数
    rc2 = re.compile(r'<div class="info-content">\s*(.*?)\s*</div>')
    req2 = rc2.findall(cont)
    #for t in req2:
    #    print(t)        #主办方 报名时间 比赛时间
    rc2 = re.compile(r'<span class="fl item-prize">\s*(.*?)\s*</span>')
    req2 = rc2.findall(cont)
    #for t in req2:
    #    print(t)        #标签
    rc2 = re.compile(r'<div class="event4-1-detail-text-box text-body clearfix">([\s\S]*?)</div>')
    req2 = rc2.findall(cont,re.S|re.M)
    #for t in req2:
    #    print(t)        #主内容
    break