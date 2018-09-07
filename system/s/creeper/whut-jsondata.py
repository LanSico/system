import re
import json

jsondata={}

taglist=['<th width="4%">学年学期</th>', '<th width="4%">学号</th>', '<th width="4%">姓名</th>', '<th width="4%">等级考试名称</th>', '<th width="4%">成绩</th>', '<th width="4%">听力成绩</th>', '<th width="4%">阅读成绩</th>', '<th width="4%">写作成 绩</th>', '<th width="4%">综合成绩</th>']
gradelist=['<tr target="sid_user" rel="66A2AB47CD677344E053FD02A8C0D1D9">\r\n\t\t\t\t\t\r\n\t\t\t\t\t<td>2017-2018-1</td>\r\n\t\t\t\t\t<td>0121603*******</td>\r\n\t\t\t\t\t<td>***</td>\r\n\t\t\t\t\t<td>国家大学英语6级</td>\r\n\t\t\t\t\t<td>367</td>\r\n\t\t\t\t\t<td>68</td>\r\n\t\t\t\t\t<td>171</td>\r\n\t\t\t\t\t<td>128</td>\r\n\t\t\t\t\t<td>0</td>\r\n\t\t\t\t</tr>', '<tr target="sid_user" rel="5818EB10E4E06802E053FD02A8C0BDEA">\r\n\t\t\t\t\t\r\n\t\t\t\t\t<td>2016-2017-2</td>\r\n\t\t\t\t\t<td>0121603490319</td>\r\n\t\t\t\t\t<td>杜俊健</td>\r\n\t\t\t\t\t<td>国家大学英语4级</td>\r\n\t\t\t\t\t<td>568</td>\r\n\t\t\t\t\t<td>204</td>\r\n\t\t\t\t\t<td>194</td>\r\n\t\t\t\t\t<td>170</td>\r\n\t\t\t\t\t<td>0</td>\r\n\t\t\t\t</tr>']


#写入查询状态和返回文本消息
jsondata["status"]="200"
jsondata["msg"]="SUCCESS"

#标签
taglists=[]
tagRegx=re.compile('<th .*?/th>')
for tag in taglist:
	taglists.append(re.sub('<.*?>','',tag))
print(taglists)

jsondata["tags"]=taglists


data=[]
gradeRegx = re.compile('<td>.*?</td>')
for gradeInfo in gradelist:
	grade = gradeRegx.findall(gradeInfo)

	gradelists={}
	for tag,info in enumerate(grade):
		gradelists[str(tag)]=re.sub('<.*?>','',info)
	data.append(gradelists)

jsondata["data"]=data
print(json.dumps(jsondata))

# {
# "status" : 0 ,          //执行状态码
# "msg"    : "SUCCESS",   //说明文字信息，没有为NULL
# "data"   :[{            //对象中嵌套数组，数组是返回的数据，
# "id"    : 1 ,
# "name"  : "xiaohong"
# },{
# "id"    : 2,
# "name"  : "xiaoming"
# }]
# }