## 高校智能赛事平台

高校智能赛事平台项目后台代码

| 环境 | Python3 |
| :---: | :---: |
| 前端 | VUE |
| 后台 | Django pymysql |
| 数据库 | MySQL |

## API文档

- [用户操作](#用户操作)
    - [注册新用户](#注册新用户)
    - [登录](#登录)
    - [登出](#登出)
    
- [资源操作](#资源操作)
    - [获取轮播图](#获取轮播图)
    - [获取一定数量的推荐比赛](#获取推荐比赛)
    - [获取一定数量的比赛列表](#获取一定数量的比赛列表)

## 用户操作
### 注册新用户 1
```
url:
    /user/
method:
    POST
params:
    *:username (formData)
    *:password (formData)
success:
    status_code=200
    json={
        "status": "true",
        "message": "账号注册成功"
    }
failure:
    status_code=400
    json={
        "error": "用户名已经存在"
    }
illegal:
    status_code=403
    json={
        "error": "非法请求"
    }
```
### 登录
```
url:
    /user/login/
method:
    POST
params:
    *:username (formData)
    *:password (formData)
success:
    status_code: 200
    json={
        "status": "true"
    }
failure:
    status_code: 400
    json={
        "error": "用户名或密码错误"
    }
failure:
    status_code: 404
    json={
        "error": "用户不存在"
    }
```
### 登出
```
url:
    /user/logout/
method:
    POST
success:
    status_code: 200
    json={
        "status": "true"
    }
failure:
    status_code: 404
    json={
        "error": "用户未登录"
    }
```    
## 资源操作
### 获取轮播图
```
url:
    /res/banner/
method:
    GET
success:
    status_code: 200
    json=[
        "title": str,
        "image": str, (url)
        "target": str, (url)
        "index": int
    ]
```
### 获取一定数量的推荐比赛
```
url:
    /res/recommend/
method:
    GET
params:
    *:num
success:
    status_code: 200
    json=[
        "title": str,
        "summary": str,
        "image": str, (url)
        "target": str, (url)
        "index": int,
        "related_user": [  
            {
                "id": int,
                "avatar": str,  # 头像缩略图
                "name": str
            }
        ]
    ]
```
### 获取一定数量的比赛列表
```
url:
    /res/contest/
method:
    GET
params:
    *:num
success:
    status_code: 200
    json=[
        "title": str,
        "sponsor": str,
        "image": str, (url)
        "target": str, (url)
        "index": int,
        "color": str,  # 修饰颜色
        "time_start": str,  # 报名时间
        "time_end": str
    ]
```
