
def is_act(path):
    
    return 3 == len(path.split('/'))

def is_cnt(path):
    return 4 == len(path.split('/'))

def is_obj(path):
    return len(path.split('/')) > 4

def is_get(method):
    return 'GET' == method

def is_put(method):
    return 'PUT' == method

def is_delete(method):
    return 'DELETE' == method

def is_head(method):
    return 'HEAD' == method

def is_post(method):
    return 'POST' == method