#coding=utf-8
#!/usr/bin/python
from importlib.machinery import SourceFileLoader

def loadFromDisk(fileName):
    name = fileName.split('/')[-1].split('.')[0]
    sp = SourceFileLoader(name, fileName).load_module().Spider()
    return sp

def run():
    sp = loadFromDisk('../plugin/py_czspp.py')  #载入本地脚本
    # formatJo = sp.init([]) # 初始化                                           
    formatJo = sp.homeContent(True) # 主页
    # formatJo = sp.homeVideoContent() # 主页视频
    # formatJo = sp.searchContent("dota",False) # 搜索
    # formatJo = sp.categoryContent('dsj','1',False,{}) # 分类
    # formatJo = sp.detailContent(["2200"]) #详情
    # formatJo = sp.playerContent("","bXZfMjIwMC1ubV8x",{}) # 播放
    print(formatJo)

if __name__ == '__main__':
    run()