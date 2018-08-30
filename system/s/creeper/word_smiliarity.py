import urllib,sys
import ssl
import http.cookiejar
import json
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

word1='乔布斯'
word2='苹果'

# client_id 为官网获取的AK， client_secret 为官网获取的SK
header={'Content-Type':'application/json; charset=UTF-8'}
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=PGi1VjLtpFn7sUnpdzf6zAGB&client_secret=tYTjgLpoOS3zhqQyL9diaeNgGCVVNRAa'
request = urllib.request.Request(host,headers=header)
response = urllib.request.urlopen(request)
content = response.read()
text = json.loads(content)
access_token =text['access_token']
header1={'Content-Type':'application/json'}
host1='https://aip.baidubce.com/rpc/2.0/nlp/v2/word_emb_vec?access_token='+access_token
data1={"word":word1}
print(data1)
data2=data=json.dumps(data1).encode('GBK')
request2 = urllib.request.Request(host1,headers=header1,data=data2)
content1 = urllib.request.urlopen(request2).read().decode("GBK")
word1_vec=[]
text = json.loads(content1)
for i in text['vec']:
	word1_vec.append(i)
data1={"word":word2}
print(data1)
data2=data=json.dumps(data1).encode('GBK')
request2 = urllib.request.Request(host1,headers=header1,data=data2)
content1 = urllib.request.urlopen(request2).read().decode("GBK")
word2_vec=[]
text = json.loads(content1)
for i in text['vec']:
	word2_vec.append(i)
c_1=0
c_2=0
c_3=0
c_4=0
for i,j in zip(word1_vec,word2_vec):
	c_1=c_1+i*j
	c_2=c_2+i*i
	c_3=c_3+j*j
	c_4=c_4+(i-j)*(i-j)
c_final=c_1/(c_2**0.5)/(c_3**0.5)
print("余弦相似度：",end='')
print(c_final)
print("欧式距离：",end='')
print(c_4**0.5)

host3='https://aip.baidubce.com/rpc/2.0/nlp/v1/topic?access_token='+access_token
data3={
	'title':word1,
	'content':word1
}
data3=data=json.dumps(data3).encode('GBK')
request3 = urllib.request.Request(host3,headers=header1,data=data3)
content3 = urllib.request.urlopen(request3).read().decode("GBK")
print(content3)
data3={
	'title':word2,
	'content':word2
}
data3=data=json.dumps(data3).encode('GBK')
request3 = urllib.request.Request(host3,headers=header1,data=data3)
content3 = urllib.request.urlopen(request3).read().decode("GBK")
print(content3)
