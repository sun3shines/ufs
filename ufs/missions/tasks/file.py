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
    
    def __init__(self):
        pass
    
    def getUrl(self):
        return strFileGet
    
class FileDelete(Task):
    
    def __init__(self):
        pass
    
    def getUrl(self):
        return strFileDelete
    
class FileHead(Task):
    
    def __init__(self):
        pass
    
    def getUrl(self):
        return strFileHead
    
class FilePost(Task):
    
    def __init__(self):
        pass
    
    def getUrl(self):
        return strFilePost
    
class FileCopy(Task):
    
    def __init__(self):
        pass
    
    def getUrl(self):
        return strFileCopy
    
class FileMove(Task):
    
    def __init__(self):
        pass
    
    def getUrl(self):
        return strFileMove
    
if __name__ == '__main__':
    
#    t = ContainerPut('she','test')
#    t = ContainerGet('she','test')
#    t = ContainerHead('she','test')
#    t = ContainerPost('she','test',quota=1024*1024*1024)
#    t = ContainerDelete('she','test')
    import pdb;pdb.set_trace()
    t = FilePut('she','test/test.txt','/root/install.log') 
    t = mission.execute(t)
    print t.status
    print t.data
        
