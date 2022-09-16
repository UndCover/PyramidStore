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
|py_cctv|央视栏目|UndCover||[添加栏目方法](#py_cctv)|
|py_bilimd|B站影视|[lm317379829](https://github.com/lm317379829)||[Cookies获取方法](#py_bilivd)|
|py_bilivd|B站视频|[lm317379829](https://github.com/lm317379829)||[Cookies获取方法](#py_bilivd)|
|py_huya|虎牙|[lm317379829](https://github.com/lm317379829)|||
|py_douyu|斗鱼|[lm317379829](https://github.com/lm317379829)|||
|py_gitcafe|小纸条|UndCover|调用py_ali||
|py_yiso|易搜|UndCover|调用py_ali||
|py_3qu|3QU|[lm317379829](https://github.com/lm317379829)|调用py_ali||
|py_cyys|创艺|[lm317379829](https://github.com/lm317379829)|调用py_ali||
|py_wmkk|完美看看|[lm317379829](https://github.com/lm317379829)| 七里香源目前无法播放||


**以上爬虫均经过测试，在保证功能完整的情况下放出，若失效，请及时反馈**

## 待测试爬虫列表
|文件名|名称|作者|描述|注意|
|---|:---:|:---:|---|---|

## 注意事项
<div id="py_ali" ></div>
<div id="py_bilivd" ></div>

* B站爬虫建议在文件对应位置填入会员/大会员cookies，以获得更好的体验。<br>
  获取方法：Chrome浏览器访问[B站](www.bilibili.com)并登陆→F12→F5→Network→Header→cookies:后面的内容。
![image](https://raw.githubusercontent.com/lm317379829/PyramidStore/main/img/cookies%E8%8E%B7%E5%8F%96.jpg)
![image](https://raw.githubusercontent.com/lm317379829/PyramidStore/main/img/py_bilivd%E5%A1%AB%E5%85%A5.jpg)

<div id="py_cctv" ></div>

* py_cctv添加分类可以访问[央视栏目](https://tv.cctv.com/lm/index.shtml)找到对应的栏目，点击栏目最新一期的链接，然后再新打开的页面里右键查看源代码。在源代码页面搜索 **videotvCodes**，找到videotvCodes的值作为栏目ID，如果videotvCodes对应的值为空，则在源代码页面搜索 **专题id**，找到TOPC开头的值即为栏目ID，最后，将栏目ID和栏目名称添加到py_cctv分类字典中即可
![image](https://raw.githubusercontent.com/UndCover/PyramidStore/main/img/cctvtopic.jpg)


