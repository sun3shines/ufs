# -*- coding: utf-8 -*-

import json
from ufs.missions.tasks.task import Task
from ufs.route.urls import  strDirPut,strDirGet,strDirDelete,strDirMove,strDirCopy
import ufs.missions.mission as mission

class DirPut(Task):
    
    def __init__(self,atName,path):
        self.atName = atName
        self.path = path
    
    def getBody(self):
        return json.dumps({'path':'/'.join([self.atName,self.path])})
    
    def getUrl(self):
        return strDirPut
    
class DirGet(Task):
    
    def __init__(self,atName,path,tree=False):
        self.atName = atName
        self.path = path
        self.tree = tree
        
    def getBody(self):
        return json.dumps({'path':'/'.join([self.atName,self.path]),
                           'tree':str(self.tree).lower()})
    
    def getUrl(self):
        return strDirGet
    
class DirDelete(Task):
    
    def __init__(self,atName,path,tree=False):
        
        self.atName = atName
        self.path = path
        self.tree = tree
    
    def getBody(self):
        return json.dumps({'path':'/'.join([self.atName,self.path]),
                           'tree':str(self.tree).lower()})
    
    def getUrl(self):
        return strDirDelete
    
class DirMove(Task):
    
    def __init__(self,atName,path,dst):
        self.atName = atName
        self.path = path
        self.dst = dst
    
    def getBody(self):
        return json.dumps({'src':'/'.join([self.atName,self.path]),
                           'dst':'/'.join([self.atName,self.dst])})
    
    def getUrl(self):
        return strDirMove
    
class DirCopy(Task):
    
    def __init__(self,atName,path,dst):
        self.atName = atName
        self.path = path
        self.dst = dst
    
    def getBody(self):
        return json.dumps({'src':'/'.join([self.atName,self.path]),
                           'dst':'/'.join([self.atName,self.dst])})
    
    def getUrl(self):
        return strDirCopy
    
    
if __name__ == '__main__':
 
#    t = DirPut('she','test/dr/dr/dr')
#    t = DirGet('she','test/cp',tree=True)
#    t = DirMove('she','test/dr','test/mv')
#    t = DirCopy('she','test/mv','test/cp')
    t = DirDelete('she','test/mv',tree=True)
    t = mission.execute(t)
    print t.status
    print t.data

