# 爬虫支持列表

|文件名|名称|作者|描述|注意|
|---|:---:|:---:|---|---|
|py_ali|阿里云盘|UndCover|用于阿里云盘爬取及阿里系爬虫调用|[个人token请搜索refresh_token进行替换](#py_ali)|
|py_zhaozy|找资源|UndCover|调用py_ali||
|py_pansou|盘搜|UndCover|调用py_ali||
|py_bilibili|哔哩哔哩|UndCover|||
|py_czspp|厂长|UndCover|||
|py_zxzj|在线资源|UndCover|||
|py_cokemv|COKEMV|UndCover|||
|py_genmov|跟剧|UndCover|||
|py_gimytv|剧迷|UndCover|||
|py_voflix|voflix|UndCover|||
|py_xmaomi|小猫咪|UndCover|||
|py_cctv|央视栏目|UndCover|||
|py_bilimd|B站影视|[lm317379829](https://github.com/lm317379829)||[Cookies获取方法](#py_bilivd)|
|py_bilivd|B站视频|[lm317379829](https://github.com/lm317379829)||[Cookies获取方法](#py_bilivd)|
|py_huya|虎牙|[lm317379829](https://github.com/lm317379829)|||
|py_douyu|斗鱼|[lm317379829](https://github.com/lm317379829)|||


**以上爬虫均经过测试，在保证功能完整的情况下放出，若失效，请及时反馈**

## 注意事项
<div id="py_ali" ></div>
<div id="py_bilivd" ></div>

* 大会员版B站爬虫需要在文件对应位置填入cookies，否则无法使用。<br>
  获取方法：Chrome浏览器访问[B站](www.bilibili.com)并登陆→F12→F5→Network→Header→cookies:后面的内容。
![image](https://raw.githubusercontent.com/lm317379829/PyramidStore/main/img/cookies%E8%8E%B7%E5%8F%96.jpg)
![image](https://raw.githubusercontent.com/lm317379829/PyramidStore/main/img/py_bilivd%E5%A1%AB%E5%85%A5.jpg)


