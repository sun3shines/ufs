# -*- coding: utf-8 -*-

from webob import Request
from ufs.route.urls import strAcountGet,strAcountPut,strAcountHead,strAcountPost,\
    strContainerGet, strContainerPut,strContainerDelete,strContainerHead,strContainerPost,\
    strFilePut,strFileGet,strFileDelete,strFileHead,strFilePost
    
import json
from cStringIO import StringIO

def actget(req):
    uenv = req.environ.copy()
    uenv['REQUEST_METHOD'] = 'POST'
    uenv['PATH_INFO'] = strAcountGet
    uenv['RAW_PATH_INFO'] = strAcountGet
    atName = req.path.split('/')[2]
    uenv['wsgi.input'] = StringIO(json.dumps({'path':atName}))
    return Request(uenv)

def actput(req):
    uenv = req.environ.copy()
    uenv['REQUEST_METHOD'] = 'POST'
    uenv['PATH_INFO'] = strAcountPut
    uenv['RAW_PATH_INFO'] = strAcountPut

    atName = req.path.split('/')[2]
    uenv['wsgi.input'] = StringIO(json.dumps({'path':atName}))
    return Request(uenv)

def actpost(req):
    uenv = req.environ.copy()
    uenv['REQUEST_METHOD'] = 'POST'
    uenv['PATH_INFO'] = strAcountPost
    uenv['RAW_PATH_INFO'] = strAcountPost

    atName = req.path.split('/')[2]
    uenv['wsgi.input'] = StringIO(json.dumps({'path':atName,'is_swift':'true'}))

    return Request(uenv) 

def acthead(req):
    uenv = req.environ.copy()
    uenv['REQUEST_METHOD'] = 'POST'
    uenv['PATH_INFO'] = strAcountHead
    uenv['RAW_PATH_INFO'] = strAcountHead

    atName = req.path.split('/')[2]
    uenv['wsgi.input'] = StringIO(json.dumps({'path':atName,'is_swift':'true'}))
    return Request(uenv)

def cntput(req):
    uenv = req.environ.copy()
    uenv['REQUEST_METHOD'] = 'POST'
    uenv['PATH_INFO'] = strContainerPut
    uenv['RAW_PATH_INFO'] = strContainerPut

    path = '/'.join(req.path.split('/')[2:])
    uenv['wsgi.input'] = StringIO(json.dumps({'path':path}))
        
    return Request(uenv)

def cntget(req):
    uenv = req.environ.copy()

    uenv['REQUEST_METHOD'] = 'POST'
    uenv['PATH_INFO'] = strContainerGet
    uenv['RAW_PATH_INFO'] = strContainerGet
    
    path = '/'.join(req.path.split('/')[2:])
    uenv['wsgi.input'] = StringIO(json.dumps({'path':path}))
    
    return Request(uenv)

def cntdel(req):
    uenv = req.environ.copy()
    uenv['REQUEST_METHOD'] = 'POST'
    uenv['PATH_INFO'] = strContainerDelete
    uenv['RAW_PATH_INFO'] = strContainerDelete

    path = '/'.join(req.path.split('/')[2:])
    uenv['wsgi.input'] = StringIO(json.dumps({'path':path}))
        
    return Request(uenv)

def cnthead(req):
    uenv = req.environ.copy()
    uenv['REQUEST_METHOD'] = 'POST'
    uenv['PATH_INFO'] = strContainerHead
    uenv['RAW_PATH_INFO'] = strContainerHead

    path = '/'.join(req.path.split('/')[2:])
    uenv['wsgi.input'] = StringIO(json.dumps({'path':path,'is_swift':'true'}))
    
    return Request(uenv)

def cntpost(req):
    uenv = req.environ.copy()
    uenv['REQUEST_METHOD'] = 'POST'
    uenv['PATH_INFO'] = strContainerPost
    uenv['RAW_PATH_INFO'] = strContainerPost

    path = '/'.join(req.path.split('/')[2:])
    uenv['wsgi.input'] = StringIO(json.dumps({'path':path}))
    
    return Request(uenv)

def objput(req):
    uenv = req.environ.copy()
    uenv['REQUEST_METHOD'] = 'POST'
    uenv['PATH_INFO'] = strFilePut
    uenv['RAW_PATH_INFO'] = strFilePut

    path = '/'.join(req.path.split('/')[2:])
    uenv['HTTP_PATH']= path
    return Request(uenv)

def objget(req):
    uenv = req.environ.copy()
    uenv['REQUEST_METHOD'] = 'POST'
    uenv['PATH_INFO'] = strFileGet
    uenv['RAW_PATH_INFO'] = strFileGet

    path = '/'.join(req.path.split('/')[2:])
    uenv['wsgi.input'] = StringIO(json.dumps({'path':path}))
        
    return Request(uenv)

def objdelete(req):
    uenv = req.environ.copy()
    uenv['REQUEST_METHOD'] = 'POST'
    uenv['PATH_INFO'] = strFileDelete
    uenv['RAW_PATH_INFO'] = strFileDelete

    path = '/'.join(req.path.split('/')[2:])
    uenv['wsgi.input'] = StringIO(json.dumps({'path':path}))
        
    return Request(uenv)

def objhead(req):
    uenv = req.environ.copy()
    uenv['REQUEST_METHOD'] = 'POST'
    uenv['PATH_INFO'] = strFileHead
    uenv['RAW_PATH_INFO'] = strFileHead

    path = '/'.join(req.path.split('/')[2:])
    uenv['wsgi.input'] = StringIO(json.dumps({'path':path,'is_swift':'true'}))

    return Request(uenv)

def objpost(req):
    uenv = req.environ.copy()
    uenv['REQUEST_METHOD'] = 'POST'
    uenv['PATH_INFO'] = strFilePost
    uenv['RAW_PATH_INFO'] = strFilePost

    path = '/'.join(req.path.split('/')[2:])
    uenv['wsgi.input'] = StringIO(json.dumps({'path':path}))
    
    return Request(uenv)    

