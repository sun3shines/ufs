# -*- coding: utf-8 -*-

import os
import os.path
import shutil

from cloudcommon.common.bufferedhttp import jresponse
from cloudcommon.common.common.swob import Response
from ufs.utils.path import listattrs

class DSt:

    def __init__(self,subject):
        self.prefix = '/mnt/storage/'
        self.subject = subject
    pass

    @property
    def path(self):
        return self.prefix + self.subject

    @property
    def exists(self):
        if os.path.exists(self.path):
            return True
        return False

    def put(self):
        try:
            os.mkdir(self.path)
            return 200
        except:
            return 409
        
    def list(self,r=False):
        # 若为文件，则获取到文件的内容了。若为dir，则获取到目录的内容。    
        return listattrs(self.path, r)

    def delete(self,r=False):

        if r:
            shutil.rmtree(self.path)
        else:
            try:
                os.rmdir(self.path)
            except:
                return 409

        return 204

    def copy(self,d):
        try:
            shutil.copytree(self.path,d.path,symlinks=True) 
            return 200
        except:
            return 400

    def move(self,d):
        try:
            shutil.move(self.path,d.path)
            return 200
        except:
            return 400

if __name__ == '__main__':
    pass
