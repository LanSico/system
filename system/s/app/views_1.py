from django.shortcuts import render
from django.http import *
from .models import Student
import re

#from django.db.models import Q
#import Q object.Document is here https://docs.djangoproject.com/en/2.1/ref/models/querysets/#django.db.models.Q

# Create your views here.


def index(request):
	return HttpResponse("1")


def user_register(request):
	if request.method == 'POST':
		u_name = request.POST.get("username")
		u_psd = request.POST.get("password")
		u_email = request.POST.get("email")
		print(u_name)
		print(u_psd)
		print(u_email)
		if checkData(u_name, u_psd, u_email):  # 检查格式
			try:
				Student.objects.get(UserName=u_name)  # 用户已存在
			except:
				try:
					Student.objects.get(Email=u_email)
				except:
					Student.objects.create(UserName=u_name, Email=u_email, PassWord=u_psd)
					return HttpResponse('{"status_code":200,"json":{"status":true,"message":"账号注册成功"}}')
				else:
					return HttpResponse('{"status_code":"400","json":{"error":"该邮箱已被注册"}}')
			else:
				return HttpResponse('{"status_code":"400","json":{"error":"用户已存在"}}')
		else:  # 非法访问
			print("test")
			return HttpResponse('{"status_code":"403","json":{"error":"非法请求"}}')
	else:  # 非法访问
		return HttpResponse('{"status_code":"403","json":{"error":"非法请求GET"}}')


def checkData(u_name, u_psd, u_email):
	if u_name and u_psd and u_email:  # 都不为空
		return True
		#if re.match(r"[]",,)
