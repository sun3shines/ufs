# -*- coding: utf-8 -*-

import os
import os.path
import shutil
from ufs.interface.meta import Meta
from ufs.utils.path import listcontainer

class ASt:
    
    def __init__(self,subject):
        
        self.subject = subject
        self.prefix = '/mnt/storage'
        self.data = {}
        self.loadm()
        
    @property
    def exists(self):
        if not os.path.exists(self.path):
            return False
        return True
    
    @property
    def path(self):
        return '/'.join([self.prefix,self.subject])
    
    @property
    def meta(self):
        return '/'.join([self.prefix,self.subject+'.meta'])
    
    def put(self):
        os.mkdir(self.path)
        self.putm({'ftype':'account',
                    'path':self.subject})
        return 200
    
    def list(self):
        return listcontainer(self.path)
    
    def delete(self):
        pass
    
    def loadm(self):
        if not self.exists:
            self.data = {}
        else:
            m = Meta(self.meta)
            self.data = m.get()
        
        return 200
    
    def putm(self,attrs):
        
        m = Meta(self.meta)
        self.data.update(attrs)
        m.put(self.data)
        return 200
    
    def getm(self):
        return self.data
    
    
    