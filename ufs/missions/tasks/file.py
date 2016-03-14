# -*- coding: utf-8 -*-

import json
from ufs.missions.tasks.task import Task
from ufs.route.urls import strFilePut,strFileGet,strFilePost, \
    strFileHead,strFileDelete,strFileCopy,strFileMove
import ufs.missions.mission as mission
from ufs.utils.md5 import md5sum

class FilePut(Task):
    
    def __init__(self,atName,path,src):
        self.atName = atName
        self.path = path
        self.src = src
    
    @property
    def md5(self):
        return md5sum(self.src)
    
    def getUrl(self):
        return strFilePut
    
    def getBody(self):
        return file(self.src)
    
    def getHeaders(self):
        return {'md5':self.md5,
                'path':'/'.join([self.atName,self.path])}
    
class MetaPut(Task):
    
    def __init__(self,atName,path,md5):
        self.atName = atName
        self.path = path
        self.md5 = md5
                
    def getUrl(self):
        return strFilePut
    
    def getHeaders(self):
        return {'datatype':'NULL',
                'path':'/'.join([self.atName,self.path]),
                'md5':self.md5}
    
    def getBody(self):
        return ''
    
    
class FileGet(Task):
    
    def __init__(self,atName,path):
        self.atName = atName
        self.path = path
    
    def getUrl(self):
        return strFileGet
    
    def getBody(self):
        return json.dumps({'path':'/'.join([self.atName,self.path])})

class FileDelete(Task):
    
    def __init__(self,atName,path):
        self.atName = atName
        self.path = path
    
    def getUrl(self):
        return strFileDelete
    
    def getBody(self):
        return json.dumps({'path':'/'.join([self.atName,self.path])})

class FileHead(Task):
    
    def __init__(self,atName,path):
        self.atName = atName
        self.path = path 
    
    def getUrl(self):
        return strFileHead
    
    def getBody(self):
        return json.dumps({'path':'/'.join([self.atName,self.path])})

class FilePost(Task):
    
    def __init__(self,atName,path,**kwargs):
        self.atName = atName
        self.path = path
        self.kwargs = kwargs
    
    def getUrl(self):
        return strFilePost
    
    def getHeaders(self):
        return self.kwargs

    def getBody(self):
        return json.dumps({'path':'/'.join([self.atName,self.path])})

class FileCopy(Task):
    
    def __init__(self,atName,path,dst):
        self.atName = atName
        self.path = path
        self.dst = dst

    
    def getUrl(self):
        return strFileCopy

    def getBody(self):
        return json.dumps({'src':'/'.join([self.atName,self.path]),
                           'dst':'/'.join([self.atName,self.dst])})    

class FileMove(Task):
    
    def __init__(self,atName,path,dst):
        self.atName = atName
        self.path = path
        self.dst = dst

    def getUrl(self):
        return strFileMove
   
    def getBody(self):
        return json.dumps({'src':'/'.join([self.atName,self.path]),
                           'dst':'/'.join([self.atName,self.dst])})
 
if __name__ == '__main__':
    
#    t = ContainerPut('she','test')
#    t = ContainerGet('she','test')
#    t = ContainerHead('she','test')
#    t = ContainerPost('she','test',quota=1024*1024*1024)
#    t = ContainerDelete('she','test')
#    t = FilePut('she','test/test.txt','/root/install.log') 
    t = MetaPut('she','test/dr/test2.txt','8dd16a3d50854caae6a23917d41688f3')
#    t = FileGet('she','test/cp.txt')
#    for data in mission.download(t):
#        print data
#        print len(data)
#    t = FileCopy('she','test/test.txt','test/cp.txt')
#    t = FileMove('she','test/test2.txt','test/mv.txt')
#    t = FilePost('she','test/mv.txt',action='move')
#    t = FileHead('she','test/mv.txt')
#    t = FileDelete('she','test/test.txt')
    t = mission.execute(t)
    print t.status
    print t.data
        
