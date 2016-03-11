
from ufs.interface.fst import FSt
def getSubject(url):
    subject = url.replace('/v1/','',1)
    return subject

class Url:
    def __init__(self,subject):
        self.prefix = '/v1/'
        self.subject = ''
 
    def getStPath(self):
        return self.url.replace(self.prefix,'',1)
        
    def getUrl(self):
        return '/'.join([self.prefix,self.subject])

def url2st(urlObj):
    return FSt(urlObj.subject)

def listUrlObj(urlObj):
    stObj = url2st(urlObj)
    pass


def setUrlObjHeader(urlObj,headers):

    stObj = url2st(urlObj)
    attrs = headers
    # attrs 和 headers 之间转化？
    return stObj.setAttrs(attrs)

def getUrlObjHeader(urlObj):
    stObj = url2st(urlObj)
    attrs = stObj.getAttrs()
    headers = attrs
    return headers 

def deleteUrlObj(path):
    pass

def downloadUrlObj(path):
    pass

