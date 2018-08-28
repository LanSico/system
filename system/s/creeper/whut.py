import requests
from time import time
import re

s=requests.Session()

def login(usn,pwd):

	header={
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language':'zh,en-US;q=0.7,en;q=0.3',
		'Accept-Encoding':'gzip, deflate',

		'Connection':'keep-alive',
		'Content-Length':'72',
		'Content-Type':'application/x-www-form-urlencoded',


		'Host':'sso.jwc.whut.edu.cn',
		'Referer':'http://sso.jwc.whut.edu.cn/Certification/toLogin.do',
		'Upgrade-Insecure-Requests':'1',

		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
	}

	data={
		'password':pwd,
		'systemId':'',
		'type':'xs',
		'userName':usn,
		'xmlmsg':''
	}

	r=s.post('http://sso.jwc.whut.edu.cn/Certification//login.do',data = data,headers = header)
	
def getGrade():
	'''header={
		'Host': '202.114.90.180',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language': 'zh,en-US;q=0.7,en;q=0.3',
		'Accept-Encoding': 'gzip, deflate',
		'Referer': 'http://sso.jwc.whut.edu.cn/Certification/login.do',
		'Connection': 'keep-alive',
		'Upgrade-Insecure-Requests': '1'
	}'''
	
	r=s.get('http://202.114.90.180/Score/')
	#r=s.get('http://202.114.90.180/Score/')
	header={
		'Host': '202.114.90.180',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
		'Accept': '*/*',
		'Accept-Language': 'zh,en-US;q=0.7,en;q=0.3',
		'Accept-Encoding': 'gzip, deflate',
		'X-Requested-With': 'XMLHttpRequest',
		'Connection': 'keep-alive'
	}
	r=s.get('http://202.114.90.180/Score/djksList.do?_='+str(int(time()*1000)),headers=header)
	dataHandle(r.text)
		
def getGrade():
	header={
		'Referer':'http://sso.jwc.whut.edu.cn/Certification//login.do',
		'Upgrade-Insecure-Requests':'1',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
	}
	r=s.get('http://202.114.90.180/Score',headers=header)
	print(r.headers)
	header={
		'Host': '202.114.90.180',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'Accept-Language': 'zh-CN,zh;q=0.9',
		'Accept-Encoding': 'gzip, deflate',
		'X-Requested-With': 'XMLHttpRequest',
		'Connection': 'keep-alive',
		'Upgrade-Insecure-Requests':'1',
		'Referer':'http://sso.jwc.whut.edu.cn/Certification//login.do'
	}
	r=s.get('http://202.114.90.180/Score/')
	print(r.headers)

def dataHandle(content):
	tagRegx=re.compile('<th .*?/th>')
	taglist=tagRegx.findall(content)
	
	for tag in taglist:
		print(re.sub('<.*?>','',tag))
	
	trRegx = re.compile('<tr target.*?/tr>',re.S)
	gradelist = trRegx.findall(content)
	
	gradeRegx = re.compile('<td>.*?</td>')
	
	for gradeInfo in gradelist:
		grade = gradeRegx.findall(gradeInfo)
		for info in grade:
			print(re.sub('<.*?>','',info))
		
	
if __name__ == '__main__':	
	login('0121603490319','djj0209')
	getGrade()