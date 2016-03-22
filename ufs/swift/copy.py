# -*- coding: utf-8 -*-

from webob import Request
from ufs.route.urls import strAcountGet,strAcountPut,strAcountHead,strAcountPost
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
