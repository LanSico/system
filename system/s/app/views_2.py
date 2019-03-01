from django.shortcuts import render
from django.http import *
import urllib
import re
import http.cookiejar
from app.models import *

#使服务器保存爬虫cookie
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)


# Create your views here.
def GetLoginInfo(request):
	u="0121603490319"
	p="095258"
	res=urllib.request.urlopen("http://zhlgd.whut.edu.cn/tpass/login?service=http://zhlgd.whut.edu.cn/tp_up/",timeout=5)
	cont=res.read().decode("utf-8")
	rc = re.compile(r'name="lt" value="(.*?)"')
	req = rc.findall(cont)
	lt=""
	for l in req:
		lt=l
	rc = re.compile(r'name="execution" value="(.*?)"')
	req = rc.findall(cont)
	execution=""
	for l in req:
		execution=l
	return render(request,"GetLoginInfo.html",{"u":u,"p":p,"lt":lt,"execution":execution})

def GetRsaKey(request):
	RsaKey=request.POST.get("rsa_result","")
	u=request.POST.get("u","")
	p=request.POST.get("p","")
	lt=request.POST.get("lt","")
	execution=request.POST.get("execution","")
	_eventId=str("submit")
	ul=str(len(u))
	pl=str(len(p))
	header={
		'Host': 'zhlgd.whut.edu.cn',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Accept-Encoding': 'gzip, deflate',
		'Referer': 'http://zhlgd.whut.edu.cn/tpass/login?service=http%3A%2F%2Fzhlgd.whut.edu.cn%2Ftp_up%2F',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Connection': 'keep-alive',
		'Upgrade-Insecure-Requests': '1',
	}
	postdata={
		'rsa':RsaKey,
		'u':u,
		'p':p,
		'lt':lt,
		'ul':ul,
		'pl':pl,
		'execution':execution,
		'_eventId':_eventId,
		}
	postdata=urllib.parse.urlencode(postdata).encode('utf-8')
	req=urllib.request.Request("http://zhlgd.whut.edu.cn/tpass/login?service=http://zhlgd.whut.edu.cn/tp_up/",data=postdata)
	res=urllib.request.urlopen(req,timeout=5)
	req=urllib.request.Request("http://zhlgd.whut.edu.cn/tpass/login?service=http://zhlgd.whut.edu.cn/tp_up/",data=postdata)
	res=urllib.request.urlopen(req,timeout=5)
	header={
		'Host': 'zhlgd.whut.edu.cn',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
		'Accept': 'text/html, */*; q=0.01',
		'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Accept-Encoding': 'gzip, deflate',
		'Referer': 'http://zhlgd.whut.edu.cn/tp_up/view?m=up',
		'X-Requested-With': 'XMLHttpRequest',
		'Connection': 'keep-alive',
	}
	req=urllib.request.Request("http://zhlgd.whut.edu.cn/tp_up/up/sysintegration/personInfo?item_id=undefined",headers=header)
	res=urllib.request.urlopen(req,timeout=5)
	header={
		'Host': 'zhlgd.whut.edu.cn',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Accept-Encoding': 'gzip, deflate',
		'Referer': 'http://zhlgd.whut.edu.cn/tp_up/view?m=up',
		'Content-Type': 'application/json;charset=utf-8',
		'Connection': 'keep-alive',
	}
	req=urllib.request.Request("http://zhlgd.whut.edu.cn/tp_up/sys/uacm/profile/getUserType",data=b'{}',headers=header)
	res=urllib.request.urlopen(req,timeout=10)
	cont=res.read().decode("utf-8")
	print(cont)
	req=urllib.request.Request("http://zhlgd.whut.edu.cn/tp_up/sys/uacm/profile/getUserByType",data=b'{"ID_NUMBER":"'+u.encode("utf-8")+b'"}',headers=header)
	res=urllib.request.urlopen(req,timeout=10)
	cont=res.read().decode("utf-8")
	print(cont)
	return HttpResponse(cont)

def index(request):
	return render(request,"index.html")

def user_login(request):
	u_name=request.POST.get("username")
	u_psd=request.POST.get("password")
	try:
		us=Student.objects.get(UserName=u_name)
	except:
		return HttpResponse('{"status_code":"404","json":{"error":"用户未激活"}}')
	try:
		us=Student.objects.get(UserName=u_name,PassWord=u_psd)
	except:
		return HttpResponse('{"status_code":"400","json":{"error":"用户名或密码错误"}}')
	else:
		request.session["user_id"]=us.User_id
		return HttpResponse('{"status_code":"200","json":{"status":“true”}}')

def user_logout(request):
	if request.session["user_id"]:
		request.session["user_id"]=""
		return HttpResponse({"status":"200","json":{"status":"true"}})
	else:
		return HttpResponse({"status":"404","json":{"error":"用户未登录"}})
		
	