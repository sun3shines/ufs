

def stp(path):
    pass

def mtp(path):
    pass

def get(req):
    subject = stp(req.path)
    stObj = FSt(subject)
    ecode = 200
    if not stObj.exists:
        ecode = 404
        return response(ecode)

    app_iter = stObj.get()
    return response(app_iter)

def put(req):
    subject = stp(req.path)
    stObj = FSt(subject)
    md5 = req.headers.get('md5')
    dataType = req.headers.get('datatype') 
    ecode = upload(stObj,md5,dataType,req.environ['wsgi.input'])
    return response(ecode)

def post(req):
    
    subject = stp(req.path)
    stObj = FSt(subject)
    if not stObj.exists:
        ecode = 404
    ecode = stObj.post(req.headers)    
    return response(ecode)

def head(req):
    # 0 表示都不存在，1表示md5存在，2表示都存在
    # 如果存在，则执行post
    # 如果不存在，则执行put
    subject = stp(req.path) 
    s = FSt(subject)
    ecode = 200
    if not stObj.exists:
        ecode = 404

    ecode = stObj.head()
    return response(ecode)

def copy(req):

    subject = stp(req.path)
    dst = stp(req.header.get('dst'))
    s = FSt(subject)
    ecode = 200
    if not s.exists:
        ecode = 404

    ecode = s.copy(dst) 
    return response(ecode)

def move(req):
    pass

def delete(req):
    pass


