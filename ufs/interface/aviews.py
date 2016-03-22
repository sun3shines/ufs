# -*- coding: utf-8 -*-

import json
import os

from cloudcommon.common.bufferedhttp import jresponse
from cloudcommon.common.common.swob import Response
from ufs.utils.path import path2o
from ufs.interface.ast import ASt

def get(req):

    param = json.loads(req.body)
    path = path2o(param.get('path'))
    a = ASt(path)
    if not a.exists:
        return Response(status=404)
    attrs = a.list()
    attrs = [{'a':'b'},{'c':'d'}] 
    return Response(body=json.dumps(attrs),status=200)

def put(req):
    
    param = json.loads(req.body)
    path = path2o(param.get('path'))
    a = ASt(path)
    if a.exists:
        return Response(status=409)
    
    ecode = a.put()
    return Response(status=ecode)    

def post(req):
    
    param = json.loads(req.body)
    path = path2o(param.get('path'))
    a = ASt(path)
    if not a.exists:
        return Response(status=404)
    
    headers = req.headers
    attrs = headers
    ecode = a.putm(attrs)
    return Response(status=ecode)

def head(req):

    param = json.loads(req.body)
    path = path2o(param.get('path'))
    is_swift = param.get('is_swift')

    a = ASt(path)
    if not a.exists:
        return Response(status=404)
    
    attrs = a.getm()
    if 'true' == is_swift:
        return Response(status=200,headers=attrs)
    return Response(body=json.dumps(attrs),status=200)


