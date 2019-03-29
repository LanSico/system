import urllib
import re
import http.cookiejar
import pymysql
import time

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
#pymysql.install_as_MySQLdb();
db = pymysql.connect("localhost", "root", "djj0209.", "cs_sys", charset='utf8')
cursor=db.cursor()

#while(True):
for page in range(1,100):
    headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }
    req=urllib.request.Request("https://www.saikr.com/vs/0/0/0?page="+str(page),headers=headers)
    res=urllib.request.urlopen(req)
    cont=res.read().decode("utf-8")
    rc = re.compile(r'<a href="(.*?)" target="_blank" title=".*?" class="link">')
    req = rc.findall(cont)
    for i in req:
        sql="INSERT INTO app_activity (Title,Kind,Level,Allower,Holder,BMStartTime,BMEndTime,CTStartTime,CTEndTime,Tag,Content,ReleaseTime,LastChangeTime) VALUES ("
        res=urllib.request.urlopen(i)
        cont=res.read().decode("utf-8")
        rc2 = re.compile(r'<h1 class="event-title">(.*?)</h1>')
        req2=rc2.findall(cont)
        sql +="'"+req2[0]+"'," #title
        rc2 = re.compile(r'<span class="title-desc">\s*(.*?)\s*</span>')
        req2 = rc2.findall(cont)
        sql +="'"+req2[1]+"'," #kind
        sql +="'"+req2[3]+"'," #level
        sql +="'"+req2[4]+"'," # allower
        rc2 = re.compile(r'<div class="info-content">\s*(.*?)\s*</div>')
        req2 = rc2.findall(cont)
        #holder
        sql+="'"
        for t in req2[:-2]:
            sql +=t+","
        sql=sql[:-1]+"',"
        rc2 = re.compile(r'<div class="info-content">\s*(.*?)\s*</div>')
        req2 = rc2.findall(cont)
        l=req2[-2:][0]
        rc3 = re.compile(r'(.*?)\&nbsp;(.*?)\&nbsp;(.*)')
        req3 = rc3.findall(l.replace(".","-"))
        sql +="'"+req3[0][0]+"'," #BMStartTime
        sql +="'"+req3[0][2]+"'," #BMEndTime
        l=req2[-1:][0]
        rc3 = re.compile(r'(.*?)\&nbsp;(.*?)\&nbsp;(.*)')
        req3 = rc3.findall(l.replace(".","-"))
        sql +="'"+req3[0][0]+"'," #CTStartTime
        sql +="'"+req3[0][2]+"'," #CTEndTime
        rc2 = re.compile(r'<span class="fl item-prize">\s*(.*?)\s*</span>')
        req2 = rc2.findall(cont[cont.find("竞赛类别"):])
        #Tag
        sql+="'"
        for t in req2:
            sql+=t+","
        sql=sql[:-1]
        sql+="',"
        rc2 = re.compile(r'<div class="event4-1-detail-text-box text-body clearfix">([\s\S]*?)</div>')
        req2 = rc2.findall(cont,re.S|re.M)
        #content
        sql+="'"
        for t in req2:
            sql+=t
        sql+="',"
        sql+="'2019-3-20 10:00','2019-3-20 10:00')" #ReleaseTime,LastChangeTime 
        cursor.execute(sql)
        db.commit()
    print(page)