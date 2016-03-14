# -*- coding: utf-8 -*-

import shutil
from ufs.interface.meta import Meta
from ufs.md5.st import MSt
import os

class FSt:
    def __init__(self,subject=''):

        self.subject = subject
        self.prefix = '/mnt/storage'
        self.data = {}
        self.loadm()

    @property
    def path(self):
        return '/'.join([self.prefix,self.subject])

    @property
    def exists(self):
        if os.path.exists(self.path):
            return True
        return False

    @property
    def md5(self):
        return self.data.get('md5')


    def loadm(self):
        
        if not os.path.exists(self.path):
            self.data = {}
        else:
            m = Meta(self.path)
            self.data = m.get()

    def setm(self,attrs={}):
        self.data.update(attrs)
        m = Meta(self.path)
        m.put(self.data)
        return 200

    def getm(self):
        return self.data 

    def put(self,md5,datatype,fileinput):

        if 'NULL' == datatype:

            if self.exists:
                if md5 == self.md5:
                    return 200
                else:
                    return 409
            else:
                if MSt(md5).exists:
                    self.setm({'md5':md5,'ftype':'f'})
                    return 200
                else:
                    return 404

        else: 
            m = MSt(md5)
            m.put(fileinput)
            self.setm({'md5':md5,'ftype':'f'})
            return 200

    def get(self):

        m = MSt(self.md5)
        return m.get()

    def delete(self):
        m = Meta(self.path)
        m.delete()

    def copy(self,d):
        shutil.copy(self.path,d.path)
        return 200

    def move(self,d):
        shutil.move(self.path,d.path)
        return 200

if __name__ == '__main__':

    md5 = 'c5371ed9133353622166fe6352b91a56'
    
    s = FSt('111')
    if s.exists:
        for data in s.get():
            print data
            print len(data)
