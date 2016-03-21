# -*- coding: utf-8 -*-

from ufs.missions.swift.task import SwiftTask
import ufs.missions.mission as mission

class AccountPut(SwiftTask):
    def __init__(self,path):
        super(AccountGet,self).__init__()
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
    def __init__(self,path):
        super(AccountGet,self).__init__()
        self.path = path
    
    def getUrl(self):
        return '/'.join(['',self.version,self.path])
    
    def getMethod(self):
        return 'POST'
    
class AccountHead(SwiftTask):
    def __init__(self,path):
        super(AccountGet,self).__init__()
        self.path = path
    
    def getUrl(self):
        return '/'.join(['',self.version,self.path])
    
    def getMethod(self):
        return 'HEAD'
   
if __name__ == '__main__':
    
    t = AccountGet('li')
    t = mission.execute(t)
    print t.status
    print t.data
 
