# -*- coding: utf-8 -*-

from ufs.missions.tasks.task import Task

class SwiftTask(Task):
    def __init__(self):
        self.version = 'v1'
        
    def getMethod(self):
        return 'GET'
    def getUrl(self):
        return ''
        
    def getBody(self):
        return ''
    
    def getHeaders(self):
        return {}
    
    def getParams(self):
        return {}
    
# 只需要关注method和url，即可,其他可不设置。

# object 中put需要关注body
