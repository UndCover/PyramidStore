
## Pyramid爬虫写法

目前所有爬虫继承spider.py(https://github.com/UndCover/PyramidStore/blob/main/tutorial/base/spider.py)
spider提供了一些需要被实现的方法和一些公共方法，请自行查阅

#### 快速开发

使用py_model.py模板可以进行快速开发(https://github.com/UndCover/PyramidStore/blob/main/tutorial/py_model.py)
模板中的所有方法都不能删掉，否则无法运行!!!
##### 1. 爬虫方法

```python
    # 这些具体的写法和Java版本的爬虫一致
    # 主页
    def homeContent(self,filter):pass
    # 推荐视频
    def homeVideoContent(self):pass
    # 分类
    def categoryContent(self,tid,pg,filter,extend):pass
    # 详情
    def detailContent(self,ids):pass
    # 搜索
    def searchContent(self,key,quick):pass
    # 播放
    def playerContent(self,flag,id,vipFlags):pass
    # 视频格式
    def isVideoFormat(self,url):pass
    # 视频检测
    def manualVideoCheck(self):pass
```

##### 2. 调用其他脚本的方法

如果在自己的脚本里需要调用其他py方法，可以参考如下写法

```python
    # 以下代码来自py_zhaozy，完整代码请自行查看 
    def getDependence(self):
        return ['py_ali']       #添加需要依赖的脚本名称到列表（需要依赖的脚本必须和当前脚本在同级目录）
    def init(self,extend):
        self.ali = extend[0]    #按依赖列表返回依赖对象
        print("============py_zhaozy============")
        pass
```
##### 3. 本地代理

代理地址写法```http://127.0.0.1:UndCover/proxy?do={key}&api=python```,其中{key}表示配置文件中key的名称,其他参数追加到地址最后即可。样例请参考py_ali.py originContent方法

```python
    # 以下代码来自py_ali，完整代码请自行查看 
    # 本地代理
    def localProxy(self,param):
        typ = param['type']
        if typ == "m3u8":
            return self.proxyM3U8(param)
        if typ == "media":
            return self.proxyMedia(param)
        return None

    def proxyMedia(self,map):
        # 略
        action = {
            'url':url,
            'header':self.header,
            'param':'',
            'type':'stream',            #数据流
            'after':''
        }
        # 若action['type'] == 'stream'，在java层请求 action['url']地址内容返回结果。
        return [200, "video/MP2T", action, ""]

    def proxyM3U8(self,map):
        shareId = map['share_id']
        fileId = map['file_id']

        shareToken = self.getToken(shareId,'')
        content = self.getMediaSlice(shareId,shareToken,fileId)
        action = {
            'url':'',
            'header':'',
            'param':'',
            'type':'string',            #文本内容
            'after':''
        }
        # 若action['type'] == 'string' 且content有内容，则直接返回结果
        # 若action['type'] == 'string' 且content位空，则在java层请求 action['url']地址内容返回结果。
        return [200, "application/octet-stream", action, content]
```
##### 4. 配置写法

* 所有文件以 py_ 开头
* api和文件名称要一致
* ext写py的网络地址或者本地地址
* 如果脚本之间有依赖关系，则脚本地址必须在同一路径下

```json
{
    "key": "py_pansou",
    "name": "盘搜",
    "type": 3,
    "api": "py_pansou",
    "searchable": 1,
    "quickSearch": 1,
    "filterable": 0,
    "ext": "file:///storage/emulated/0/plugin/py_pansou.py"
}, {
    "key": "push_agent",
    "name": "阿里",
    "type": 3,
    "api": "py_ali",
    "searchable": 0,
    "quickSearch": 0,
    "filterable": 0,
    "ext": "file:///storage/emulated/0/plugin/py_ali.py"
}
```
##### 5. 外置参数

* spider内置一个extend参数，用于接收配置链接中的extend参数

```json
{
    "key": "push_agent",
    "name": "阿里",
    "type": 3,
    "api": "py_ali",
    "searchable": 0,
    "quickSearch": 0,
    "filterable": 0,
    "ext": "https://raw.githubusercontent.com/UndCover/PyramidStore/main/plugin/py_ali.py?extend=12345678901234561234567890123456"  //外置参数传递
}
```

```python
def login(self):
        self.localTime = int(time.time())
        url = 'https://api.aliyundrive.com/token/refresh'
        if len(self.authorization) == 0 or self.timeoutTick - self.localTime <= 600:
            form = {
                'refresh_token':'b566279f7cd98ba3b566279f7cd98ba3'              
            }
            try:
                if len(self.extend) > 0:
                    form['refresh_token'] = self.extend     #使用外置参数作为token
            except Exception as e:
                pass
            rsp = requests.post(url,json = form,headers=self.header)
            jo = json.loads(rsp.text)
            if rsp.status_code == 200:
                self.authorization = jo['token_type'] + ' ' + jo['access_token']
                self.expiresIn = int(jo['expires_in'])
                self.timeoutTick = self.localTime + self.expiresIn
                return True
            return False
        else:
            return True
```

##### 问题请反馈到[tg](https://t.me/+A3SLQRmPVi9kOThl)群里