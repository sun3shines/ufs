
from core.mem import Mem

class FMem(Mem):
    # 大metadata结构，都是经过metadata的，而不是绕过了。所以不搞md5和path
    def __init__(self,subject):

        super(FSets,self).__init__()
        self.subject = subject
        self.siffix = '.meta'
        self.md5 = 'md5'

    def setMd5(val):
        self.setMeta(self.md5,val)

    def getMd5():
        return self.getMeta(self.path)

    def loadData():
        pass

    def getData():
        return self.getMeta()

def mem2md5(memObj):
    return Md5(memObj.getMd5())



