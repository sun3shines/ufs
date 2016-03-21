# -*- coding: utf-8 -*-

from webob import Request
from ufs.route.urls import strAcountGet,strAcountPut,strAcountHead,strAcountPost
import json
from cStringIO import StringIO

def actget(req):
    uenv = req.envrion.copy()
    uenv['REQUEST_METHOD'] = 'POST'
    uenv['PATH_INFO'] = strAcountGet
    uenv['RAW_PATH_INFO'] = strAcountGet
    atName = req.path.split('/')[2]
    uenv['wsgi.input'] = StringIO(json.dumps({'path':atName}))
    return Request(uenv)


