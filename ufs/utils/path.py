# -*- coding: utf-8 -*-

import os.path
from ufs.interface.meta import Meta
prefix = ''

def path2o(path):

    return path

def path2a(path):

    return path

def path2c(path):

    return path

def listattrs(path,r=False):
    
    attrs = []
    for obj in os.listdir(path):
        fullpath = '/'.join([path,obj])
        if os.path.isfile(fullpath):
            attr = Meta(fullpath).get()
            attr.update({'path':obj})
        elif os.path.isdir(fullpath):
            attr = {'ftype':'d',
                    'path':obj}
            if r:
                attr.update({'list':listattrs(fullpath, r)})
            
        elif os.path.islink(fullpath):
            attr = {'ftype':'f',
                    'path':'l'}
        attrs.append(attr)
        
    return attrs

def listcontainer(path):
    
    attrs = []
    for obj in os.listdir(path):
        fullpath = '/'.join([path,obj])
        if os.path.isfile(fullpath) and fullpath.endswith('.meta'):
            attr = Meta(fullpath).get()
            attr.update({'path':obj})
            attrs.append(attr)
    
    return attrs

if __name__ == '__main__':

    print listattrs('test',True) 
