# -*- coding: utf-8 -*-

import json
import os

from cloudcommon.common.bufferedhttp import jresponse
from cloudcommon.common.common.swob import Response
from ufs.utils.path import path2o
from ufs.interface.cst import CSt

def get(req):
    
    param = json.loads(req.body)
    path = path2o(param.get('path'))
    tree = param.get('tree')
    if 'true' == tree:
        r = True
    else:
        r = False
        
    c = CSt(path)
    if not c.exists:
        return Response(status=404)

    attrs = c.list(r)
    return Response(body = json.dumps(attrs),status=200)

def put(req):
    
    param = json.loads(req.body)
    path = path2o(param.get('path'))
    
    c = CSt(path)
    if c.exists:
        return Response(status=409)    

    ecode = c.put()
    return Response(status=ecode)

def delete(req):
    
    param = json.loads(req.body)
    path = path2o(param.get('path'))
    
    c = CSt(path)
    if not c.exists:
        return Response(status=404)
    
    ecode = c.delete()
    return Response(status=ecode)

def head(req):
    
    param = json.loads(req.body)
    path = path2o(param.get('path'))
 
    c = CSt(path)
    if not c.exists:
        return Response(status=404)
    
    attrs = c.getm()
    return Response(body = json.dumps(attrs),status=200)   

def post(req):
    
    param = json.loads(req.body)
    path = path2o(param.get('path'))
    
    c = CSt(path)
    if not c.exists:
        return Response(status=404)
    
    headers = req.headers
    attrs = headers
    ecode = c.putm(attrs)
    return Response(status = ecode)
    
    