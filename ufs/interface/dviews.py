# -*- coding: utf-8 -*-

import json
import os

from cloudcommon.common.bufferedhttp import jresponse
from cloudcommon.common.common.swob import Response
from ufs.utils.path import path2o
from ufs.interface.dst import DSt

def put(req):
    
    param = json.loads(req.body)
    path = path2o(param.get('path'))
    d = DSt(path)
    
    if d.exists:
        return Response(status=409)
    ecode = d.put()
    return Response(status=ecode)

def get(req):

    param = json.loads(req.body)
    path = path2o(param.get('path'))
    tree = param.get('tree')
    if 'true' == tree:
        r = True
    else:
        r = False
        
    d = DSt(path)    
    if not d.exists:
        return Response(status=404)
    if not os.path.isdir(d.path):
        return Response(body = 'path type error',status=400)
    attrs = d.list(r)
    return Response(body = json.dumps(attrs),status=200)
    

def delete(req):
    
    param = json.loads(req.body)
    path = path2o(param.get('path'))
    tree = param.get('tree')
    if 'true' == tree:
        r = True
    else:
        r = False
         
    d = DSt(path)
    ecode = d.delete(r)
    return Response(status = ecode)

def copy(req):
    
    param = json.loads(req.body)
    src = path2o(param.get('src'))
    dst = path2o(param.get('dst'))
    s = DSt(src)
    d = DSt(dst)
    ecode = s.copy(d)
    return Response(status = ecode)

def move(req):
    
    param = json.loads(req.body)
    src = path2o(param.get('src'))
    dst = path2o(param.get('dst'))
    s = DSt(src)
    d = DSt(dst)
    ecode = s.move(d)
    return Response(status = ecode)


