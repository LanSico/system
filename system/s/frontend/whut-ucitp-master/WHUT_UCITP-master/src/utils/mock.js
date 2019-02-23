import Mock from 'mockjs' // 引入mockjs
 
const Random = Mock.Random // 获取 mock.Random 对象

const url = {
  banners:'/banners',
  recommend: '/recommend',
  contests:'/contests'
}

let banners={
  'banners|3':
  [
    {
      'id|+1':0,
      'link|+1':[
        'https://www.baidu.com/s?wd=中国大学生计算机设计大赛',
        'https://www.baidu.com/s?wd=大学生UI设计大赛',
        'https://www.baidu.com/s?wd=全国logo设计大赛'
      ],
      'bgImg':{
        'backgroundImage|+1':[
          'url(https://s2.ax1x.com/2019/02/23/khVfRs.jpg)',
          'url(https://s2.ax1x.com/2019/02/23/khk3Kf.png)',
          'url(https://s2.ax1x.com/2019/02/23/khklxP.png)'
        ],
      },
      'src|+1':[
        'https://s2.ax1x.com/2019/02/23/khVfRs.jpg',
        'https://s2.ax1x.com/2019/02/23/khk3Kf.png',
        'https://s2.ax1x.com/2019/02/23/khklxP.png'
      ],
      'bannerText|+1':[
        '第十二届中国大学生计算机设计大赛',
        '第一届大学生UI设计大赛',
        '第二届全国LOGO设计大赛'
      ]
    }
  ]
}

let recommenList = {
  'recommenList|3':
  [
    {
      'id|+1':0,
      'title|+1':[
        '互联网+',
        'RoboMaster',
        'SAS数据分析大赛'
      ],
      'picUrl|+1':[
        'https://s2.ax1x.com/2019/02/22/kfWeDH.jpg',
        'https://s2.ax1x.com/2019/02/22/kfWd5q.jpg',
        'https://s2.ax1x.com/2019/02/22/kfWM5t.jpg'
      ],
      'introduce|+1':[
        '“互联网+”，就是“互联网+各个传统行业”。但这并不是简单的两者相加，而是利用信息通信技术以及互联网平台，让互联网与传统行业进行深度融合，创造新的发展生态。它代表一种新的社会形态。',
        'RoboMaster（全国大学生机器人大赛），是中国最具影响力的机器人项目，包含机器人赛事、机器人生态、以及工程文化等多项内容，正在全球范围内掀起一场机器人科技狂潮。',
        'SAS数据分析大赛，是由SAS中国公司发起的专门针对中国高校数据分析相关专业的一次非盈利性的公益大赛。由SAS中国主办，授权由数学中国网合作推广。'
      ],
      'participants|3-5':[
        {
        'picUrl|+1':[
          'https://s2.ax1x.com/2019/02/22/kfWEvD.jpg',
          'https://s2.ax1x.com/2019/02/22/kfWAgO.jpg',
          'https://s2.ax1x.com/2019/02/22/kfWk8K.jpg',
          'https://s2.ax1x.com/2019/02/22/kfWFC6.jpg',
          'https://s2.ax1x.com/2019/02/22/kfWP4x.jpg',
          'https://s2.ax1x.com/2019/02/22/kfWCU1.jpg',
          'https://s2.ax1x.com/2019/02/22/kfW9ER.jpg',
          'https://s2.ax1x.com/2019/02/22/kfWSb9.jpg',
          'https://s2.ax1x.com/2019/02/22/kfRzDJ.jpg',
          'https://s2.ax1x.com/2019/02/22/kfRjvF.jpg',
          'https://s2.ax1x.com/2019/02/22/kfRXgU.jpg',
          'https://s2.ax1x.com/2019/02/22/kfRO3T.jpg'
        ]
        }
      ]
    }
  ],
}

let contests = {
  'contest|9':
  [
    {
      'id|+1':0,
      'title|+1':[
        '广告艺术大赛',
        'NECCS',
        '计算机设计大赛',
        '海报设计大赛',
        'LOGO设计大赛',
        '创意摄影大赛',
        '全国书法大赛',
        '原创歌曲征集大赛',
        '全国漫画大赛'
      ],
      /*
      'picUrl':Random.image('200x100', '#1E1E1E', '#FFF', '-'),
      */
      'picUrl|+1':[
        'https://s2.ax1x.com/2019/02/22/kfRxu4.jpg',
        'https://s2.ax1x.com/2019/02/22/kfW8xS.jpg',
        'https://s2.ax1x.com/2019/02/22/kfWlPP.jpg',
        'https://s2.ax1x.com/2019/02/22/kfWtbj.jpg',
        'https://s2.ax1x.com/2019/02/22/kfWUVs.jpg',
        'https://s2.ax1x.com/2019/02/22/kfW18f.jpg',
        'https://s2.ax1x.com/2019/02/22/kfWJKg.jpg',
        'https://s2.ax1x.com/2019/02/22/kfWaan.jpg',
        'https://s2.ax1x.com/2019/02/22/kfWKUI.jpg',
      ],
      'host|+1':[
        '教育部',
        '外部教学研究会',
        '教育部',
        '中国知识产权报社',
        '信息管理协会',
        '中国摄协',
        '中国硬笔书法协会',
        '中国青年报社',
        '美术家协会漫画艺委会'
      ],
      'color|+1':[
        '#f08e5f',
        '#5f92f0',
        '#6bf05f',
        '#09d2f0',
        '#e1001a',
        '#bfcdbe',
        '#c1ad95',
        '#3e1416',
        '#8491a2'
      ],
      'percent|+1':[
        '50',
        '31',
        '43',
        '21',
        '45',
        '67',
        '73',
        '25',
        '51'
      ],
      'periods|2':[
        {
        'id|+1':0,
        'time':Random.datetime('yyyy-MM-dd')
        }
      ]
    }
  ]

}
 
Mock.mock(url.banners, 'post',banners) // 模拟banner列表
Mock.mock(url.recommend, 'post',recommenList) // 模拟推荐列表
Mock.mock(url.contest, 'post',contests) // 模拟比赛列表

/*

    'Boolean': Random.boolean, // 可以生成基本数据类型
    'Natural': Random.natural(1, 10), // 生成1到10之间自然数
    'Integer': Random.integer(1, 100), // 生成1到100之间的整数
    'Float': Random.float(0, 100, 0, 5), // 生成0到100之间的浮点数,小数点后尾数为0到5位
    'Character': Random.character(), // 生成随机字符串,可加参数定义规则
    'String': Random.string(2, 10), // 生成2到10个字符之间的字符串
    'Range': Random.range(0, 10, 2), // 生成一个随机数组
    'Date': Random.date(), // 生成一个随机日期,可加参数定义日期格式
    'Image': Random.image(Random.size, '#02adea', 'Hello'), // Random.size表示将从size数据中任选一个数据
    'Color': Random.color(), // 生成一个颜色随机值
    'Paragraph':Random.paragraph(2, 5), //生成2至5个句子的文本
    'Name': Random.name(), // 生成姓名
    'Url': Random.url(), // 生成web地址
    'Address': Random.province() // 生成地址

*/