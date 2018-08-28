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
	header={
		'Referer':'http://sso.jwc.whut.edu.cn/Certification//login.do',
		'Upgrade-Insecure-Requests':'1',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
	}
	r=s.get('http://202.114.90.180/Score',headers=header)
	#print(r.headers)
	
	r=s.get('http://202.114.90.180/Score/')
	print(r.headers)
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

def dataHandle(content):
	tagRegx=re.compile('<th .*?/th>')
	taglist=tagRegx.findall(content)
	
	for tag in taglist:
		print(re.sub('<.*?>','',tag))#学年 学期 学号 姓名 等级考试名称 成绩 听力成绩 阅读成绩 写作成绩 综合成绩
	
	trRegx = re.compile('<tr target.*?/tr>',re.S)
	gradelist = trRegx.findall(content)
	
	gradeRegx = re.compile('<td>.*?</td>')
	
	for gradeInfo in gradelist:
		grade = gradeRegx.findall(gradeInfo)
		for info in grade:
			print(re.sub('<.*?>','',info))
	'''
	{
		{'status':1,'tag1':'',....},
		{'status':2,'tag2':'',....},
		{.......				  }
	}
	'''
			
		
	
if __name__ == '__main__':	
	login('0121603490319','djj0209')
	getGrade()