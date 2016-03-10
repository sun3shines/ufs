# -*- coding: utf-8 -*-

import os
import os.path
import shutil

from cloudcommon.common.bufferedhttp import jresponse
from cloudcommon.common.common.swob import Response
from ufs.utils.path import listattrs
from ufs.interface.meta import Meta

class CSt:
    
    def __init__(self,subject):
        self.prefix = '/mnt/storage/'
        self.subject = subject
        self.data = {}
        self.loadm()
        
    @property
    def path(self):
        return self.prefix + self.subject

    @property
    def meta(self):
        return '/'.join([self.prefix,self.subject+'.meta' ])
    
    @property
    def exists(self):
        if os.path.exists(self.path):
            return True
        return False

    def put(self):
        try:
            os.mkdir(self.path)
            self.putm({'ftype':'container'})
            return 200
        except:
            return 409
        
    def list(self,r=False):
        # 若为文件，则获取到文件的内容了。若为dir，则获取到目录的内容。    
        return listattrs(self.path, r)

    def delete(self):
        
        try:
            os.rmdir(self.path)
            Meta(self.meta).delete()
        except:
            return 409

        return 204
        
    def loadm(self):
    
        if not os.path.exists(self.path):
            self.data = {}
        else:
            m = Meta(self.meta)
            self.data = m.get()
        
    def putm(self,attrs):
        self.data.update(attrs)
        m = Meta(self.meta)
        m.put(self.data)
        return 200
    
    def getm(self):
        m = Meta(self.meta)
        return m.get()
        