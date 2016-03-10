

from ufs.utils.path import stp

def get(req):
    subject = stp(req.path)
    s = FSt(subject)
    ecode = 200
    if not s.exists:
        ecode = 404
        return response(ecode)

    app_iter = s.get()
    return response(app_iter)

def put(req):
    subject = stp(req.path)
    s = FSt(subject)
    md5 = req.headers.get('md5')
    datatype = req.headers.get('datatype') 
    input = req.environ['wsgi.input']
    ecode = s.put(md5,datatype,input)
    return response(ecode)

def post(req):
    
    path = stp(req.path)
    s = FSt(path)
    if not s.exists:
        ecode = 404
    attrs = req.headers
    ecode = s.setm(attrs)    
    return response(ecode)

def head(req):

    path = stp(req.path) 
    s = FSt(path)
    ecode = 200
    if not s.exists:
        ecode = 404

    data = s.getm()
    return response(ecode,data)

def copy(req):

    src = stp(req.path)
    dst = stp(req.header.get('dst'))
    s = FSt(src)
    d = FSt(dst)
    ecode = 200
    if not s.exists:
        ecode = 404

    ecode = s.copy(d)
    return response(ecode)

def move(req):

    src = stp(req.path)
    dst = stp(req.header.get('dst'))
    s = FSt(src)
    d = FSt(dst)
    ecode = 200
    if not s.exists:
        ecode = 404

    ecode = s.move(d)
    return response(ecode)

def delete(req):
   
    path = stp(req.path)
    s = FSt(path)
    s.delete()

    ecode = 204
    return response(ecode) 

