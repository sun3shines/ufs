# -*- coding: utf-8 -*-

from ufs.missions.swift.task import SwiftTask
import ufs.missions.mission as mission

class AccountPut(SwiftTask):
    def __init__(self,path):
        super(AccountPut,self).__init__()
        self.path = path
    
    def getUrl(self):
        return '/'.join(['',self.version,self.path])
    
    def getMethod(self):
        return 'PUT'
    
class AccountGet(SwiftTask):
    def __init__(self,path):
        super(AccountGet,self).__init__()
        self.path = path
    
    def getUrl(self):
        return '/'.join(['',self.version,self.path])
    
    def getMethod(self):
        return 'GET'
    
class AccountPost(SwiftTask):
    def __init__(self,path,**kwargs):
        super(AccountPost,self).__init__()
        self.path = path
        self.kwargs = kwargs
        
    def getUrl(self):
        return '/'.join(['',self.version,self.path])
    
    def getMethod(self):
        return 'POST'
    
    def getHeaders(self):
        return self.kwargs
    
class AccountHead(SwiftTask):
    def __init__(self,path):
        super(AccountHead,self).__init__()
        self.path = path
    
    def getUrl(self):
        return '/'.join(['',self.version,self.path])
    
    def getMethod(self):
        return 'HEAD'
   
if __name__ == '__main__':
    
#    t = AccountGet('li')
#    t = AccountPut('li')
#    t = AccountHead('li')
    t = AccountPost('li',quota=100)
    import pdb;pdb.set_trace()
    t = mission.execute(t)
    print t.status
    print t.data
    print t.headers
 
