# -*- coding: utf-8 -*-

from ufs.swift.path import is_act,is_cnt,is_obj,is_get,\
    is_put,is_head,is_post,is_delete
    
from ufs.swift.copy import actget,actput,actpost,acthead,\
    cntput,cntget,cntdel,cnthead,cntpost,\
    objput,objget,objdelete,objhead,objpost
    
def is_swift(path):
    return path.startswith('/v1')

def swift2ufs(req):
    
    if is_act(req.path):
        if is_get(req.method):
            return actget(req)
        elif is_put(req.method):
            return actput(req)
        elif is_head(req.method):
            return acthead(req)
        elif is_post(req.method):
            return actpost(req)
        else:
            return None
    elif is_cnt(req.path):
        if is_get(req.method):
            return cntget(req)
        elif is_put(req.method):
            return cntput(req)
        elif is_delete(req.method):
            return cntdel(req)
        elif is_head(req.method):
            return cnthead(req)
        elif is_post(req.method):
            return cntpost(req)
        else:
            return None        

    elif is_obj(req.path):
        if is_get(req.method):
            return objget(req)
        elif is_put(req.method):
            return objput(req)
        elif is_delete(req.method):
            return objdelete(req)
        elif is_head(req.method):
            return objhead(req)
        elif is_post(req.method):
            return objpost(req)
        else:
            return None        
        
    return None

