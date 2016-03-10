# -*- coding: utf-8 -*-

import json

from cloudcommon.common.bufferedhttp import jresponse
from cloudcommon.common.common.swob import Response
from ufs.utils.path import path2o
from ufs.interface.fst import FSt

def get(req):
    param = json.loads(req.body)
    
    path = path2o(param.get('path'))
    s = FSt(path)
    if not s.exists:
        return Response(status=404)

    app_iter = s.get()
    response = Response(app_iter=app_iter,request=req, conditional_response=True,range=range)
    return req.get_response(response)

def put(req):
    
    param = req.headers
    path = path2o(param.get('path'))
    s = FSt(path)
    
    md5 = req.headers.get('md5')
    datatype = req.headers.get('datatype') 
    fileinput = req.environ['wsgi.input']
    ecode = s.put(md5,datatype,fileinput)
    
    return Response(status=ecode)

def post(req):
    
    param = json.loads(req.body)
    path = path2o(param.get('path'))
    
    s = FSt(path)
    if not s.exists:
        return Response(status = 404)
    attrs = req.headers
    ecode = s.setm(attrs)    
    return Response(status=ecode)

def head(req):

    param = json.loads(req.body)
    path = path2o(param.get('path')) 
    s = FSt(path)
    
    if not s.exists:
        ecode = 404
        return Response(ecode)
    data = s.getm()
    return Response(json.dumps(data),status=ecode)

def copy(req):

    param = json.loads(req.body)
    src = path2o(param.get('src'))
    dst = path2o(param.get('dst'))
    s = FSt(src)
    d = FSt(dst)
    if not s.exists:
        return Response(status=404)

    ecode = s.copy(d)
    return Response(status = ecode)

def move(req):

    param = json.loads(req.body)
    src = path2o(param.get('src'))
    dst = path2o(param.get('dst'))
    
    s = FSt(src)
    d = FSt(dst)
    
    if not s.exists:
        return Response(status=404)
        
    ecode = s.move(d)
    return Response(status=ecode)

def delete(req):
   
    param = json.loads(req.body)
    path = path2o(param.get('path')) 
    
    s = FSt(path)
    ecode = s.delete()
    
    return Response(status=ecode) 

