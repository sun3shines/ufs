# -*- coding: utf-8 -*-

from ufs.missions.swift.task import SwiftTask
import ufs.missions.mission as mission

class ContainerPut(SwiftTask):
    def __init__(self,path):
        super(ContainerPut,self).__init__()
        self.path = path
        
    def getUrl(self):
        return '/'.join(['',self.version,self.path])
    def getMethod(self):
        return 'PUT'
    
class ContainerGet(SwiftTask):
    def __init__(self,path):
        super(ContainerGet,self).__init__()
        self.path = path
        
    def getUrl(self):
        return '/'.join(['',self.version,self.path])
    def getMethod(self):
        return 'GET'
            
class ContainerDelete(SwiftTask):
    def __init__(self,path):
        super(ContainerDelete,self).__init__()
        self.path = path
        
    def getUrl(self):
        return '/'.join(['',self.version,self.path])
    def getMethod(self):
        return 'DELETE'
            
class ContainerPost(SwiftTask):
    def __init__(self,path,**kwargs):
        super(ContainerPost,self).__init__()
        self.path = path
        self.kwargs = kwargs
        
    def getUrl(self):
        return '/'.join(['',self.version,self.path])
    def getMethod(self):
        return 'POST'
    
    def getHeaders(self):
        return self.kwargs
    
class ContainerHead(SwiftTask):
    def __init__(self,path):
        super(ContainerHead,self).__init__()
        self.path = path
        
    def getUrl(self):
        return '/'.join(['',self.version,self.path])
    def getMethod(self):
        return 'HEAD'
    
if __name__ == '__main__': 

#    t = ContainerGet('li/test')
    t = ContainerPut('li/test')
#    t = ContainerHead('li/test')
#    t = ContainerPost('li/test',cquota=100)
#    t = ContainerDelete('li/test')
#    import pdb;pdb.set_trace()
    t = mission.execute(t)
    print t.status
    print t.data
    print t.headers

