# -*- coding: utf-8 -*-

import json
from ufs.missions.tasks.task import Task
from ufs.route.urls import strContainerPut,strContainerGet,strContainerPost, \
    strContainerHead,strContainerDelete
import ufs.missions.mission as mission

class ContainerPut(Task):
    
    def __init__(self,atName,path):
        self.atName = atName
        self.path = path

    def getBody(self):
        return json.dumps({'path':'/'.join([self.atName,self.path])})
    
    def getUrl(self):
        return strContainerPut
    
class ContainerGet(Task):
    
    def __init__(self,atName,path,tree='false'):
        self.atName = atName
        self.path = path
        self.tree = tree
        
    def getBody(self):
        return json.dumps({'path':'/'.join([self.atName,self.path]),
                           'tree':self.tree})
    
    def getUrl(self):
        return strContainerGet
    
class ContainerDelete(Task):
    
    def __init__(self,atName,path):
        self.atName = atName
        self.path = path

    def getBody(self):
        return json.dumps({'path':'/'.join([self.atName,self.path])})
    
    def getUrl(self):
        return strContainerDelete
    
class ContainerHead(Task):
    
    def __init__(self,atName,path):
        self.atName = atName
        self.path = path

    def getBody(self):
        return json.dumps({'path':'/'.join([self.atName,self.path])})
    
    def getUrl(self):
        return strContainerHead
    
class ContainerPost(Task):
    
    def __init__(self,atName,path,**kwargs):
        self.atName = atName
        self.path = path
        self.kwargs = kwargs
        
    def getHeaders(self):
        return self.kwargs
    
    def getBody(self):
        return json.dumps({'path':'/'.join([self.atName,self.path])})
    
    def getUrl(self):
        return strContainerPost
    
if __name__ == "__main__": 

    t = ContainerPut('she','test')
#    t = ContainerGet('she','test')
#    t = ContainerHead('she','test')
#    t = ContainerPost('she','test',quota=1024*1024*1024)
#    t = ContainerDelete('she','test')
    t = mission.execute(t)
    print t.status
    print t.data
