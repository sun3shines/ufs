# -*- coding: utf-8 -*-

from ufs.swift.path import is_act,is_cnt,is_obj,is_get,\
    is_put,is_head,is_post,is_delete
    
from ufs.swift.copy import actget
def is_swift(path):
    return path.startswith('/v1')

def swift2ufs(req):
    
    if is_act(req.path):
        if is_get(req.mehtod):
            return actget(req)
        elif is_put(req.mehtod):
            return None
        elif is_head(req.mehtod):
            return None
        elif is_post(req.method):
            return None
        else:
            return None
        
    return req

