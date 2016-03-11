# -*- coding: utf-8 -*-

import json
from ufs.missions.tasks.task import Task
from ufs.route.urls import strAcountPut,strAcountGet,strAcountPost,strAcountHead
import ufs.missions.mission as mission
class AccountPut(Task):    
    
    def __init__(self,atName):
        self.atName = atName
        
    
    def getBody(self):
        return json.dumps({'path':self.atName})
    
    def getHeaders(self):
        return {}
    
    def getUrl(self):
        return strAcountPut
    
class AccountGet(Task):    
    
    def __init__(self,atName):
        self.atName = atName
        
    
    def getBody(self):
        return json.dumps({'path':self.atName})
    
    def getHeaders(self):
        return {}
    
    def getUrl(self):
        return strAcountGet
    
class AccountPost(Task):    
    
    def __init__(self,atName,**kwargs):
        self.atName = atName
        self.kwargs = kwargs
    def getBody(self):
        return json.dumps({'path':self.atName})
    
    def getHeaders(self):
        return self.kwargs
    
    def getUrl(self):
        return strAcountPost
    
class AccountHead(Task):    
    
    def __init__(self,atName):
        self.atName = atName
        
    
    def getBody(self):
        return json.dumps({'path':self.atName})
    
    def getHeaders(self):
        return {}
    
    def getUrl(self):
        return strAcountHead
       
    

if __name__ == "__main__": 

    import pdb;pdb.set_trace()
#    t = AccountPut('she')
    t = AccountGet('she')
#    t = AccountHead('she')
#    t = AccountPost('she',quota=1024*1024*1024)

    t = mission.execute(t)
    print t.status
    print t.data

