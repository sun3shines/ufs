# -*- coding: utf-8 -*-

from ufs.missions.swift.task import SwiftTask
import ufs.missions.mission as mission
from ufs.utils.md5 import md5sum

class ObjectPut(SwiftTask):
    def __init__(self,path,src):
        super(ObjectPut,self).__init__()
        self.path = path
        self.src = src
        
    @property
    def md5(self):
        return md5sum(self.src)
    
    def getMethod(self):
        return 'PUT'
    
    def getUrl(self):
        return '/'.join(['',self.version,self.path])
    
    def getBody(self):
        return file(self.src)
    
    def getHeaders(self):
        return {'md5':self.md5}
    
class ObjectGet(SwiftTask):
    def __init__(self,path):
        super(ObjectGet,self).__init__()
        self.path = path
        
    def getMethod(self):
        return 'GET'
    
    def getUrl(self):
        return '/'.join(['',self.version,self.path])
    
class ObjectDelete(SwiftTask):
    def __init__(self,path):
        super(ObjectDelete,self).__init__()
        self.path = path
        
    def getMethod(self):
        return 'DELETE'
    
    def getUrl(self):
        return '/'.join(['',self.version,self.path])
    
class ObjectHead(SwiftTask):
    def __init__(self,path):
        super(ObjectHead,self).__init__()
        self.path = path
        
    def getMethod(self):
        return 'HEAD'
    
    def getUrl(self):
        return '/'.join(['',self.version,self.path])
    
class ObjectPost(SwiftTask):
    def __init__(self,path,**kwargs):
        super(ObjectPost,self).__init__()
        self.path = path
        self.kwargs = kwargs
        
    def getMethod(self):
        return 'POST'
    
    def getUrl(self):
        return '/'.join(['',self.version,self.path])
    
    def getHeaders(self):
        return self.kwargs

if __name__ == '__main__':

#    t = ObjectGet('li/test/obj.txt')
#    t = ObjectPut('li/test/obj.txt','/root/install.log')
#    t = ObjectHead('li/test/obj.txt')
#    t = ObjectPost('li/test/obj.txt',oquota=100)
    t = ObjectDelete('li/test/obj.txt')
#    import pdb;pdb.set_trace()
    t = mission.execute(t)
    print t.status
    print t.data
    print t.headers

