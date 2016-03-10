# -*- coding: utf-8 -*-

import shutil
from ufs.interface.meta import Meta
from ufs.md5.st import MSt
import os

class FSt:
    def __ini__(self,subject=''):

        self.subject = subject
        self.prefix = '/mnt/storage/'
        self.data = {'md5':md5}
        self.load()

    @property
    def path(self):
        return self.subject+self.prefix

    @property
    def exists(self):
        if os.path.exists(self.path):
            return True
        return False

    @property
    def md5(self):
        return self.data.get('md5')


    def load():
        m = Meta(self.path)
        self.data = m.get()

    def setm(self,attrs={}):
        self.data.update(attrs)
        m = Meta(self.path)
        m.put(self.data)

    def getm(self):
        return self.data 

    def put(self,md5,datatype,input):
        if 'NULL' == datatype:

            if self.exists:
                if md5 == self.md5:
                    return 200
                else:
                    return 409
            else:
                if MSt(md5).exists:
                    self.setm({'md5':md5,'ftype':'f'})
                    return 200
                else:
                    return 404

        else: 
            m = MSt(self.md5)
            return m.put(input)

    def get(self):

        md = MSt(self.md5)
        return m.get()

    def delete(self):
        m = Meta(self.path)
        m.delete()

    def copy(self,d):
        shutil.copy(self.path,d.path)

    def move(self,d):
        shutil.move(self.path,d.path)

if __name__ == '__main__':

    md5 = 'c5371ed9133353622166fe6352b91a56'
    
    s = FSt('111')
    if exists(s):
        download(s)


#def st2md5(stObj):
#    return stObj.getMd5Obj()

#def plxOp(stObj):
    # stObj.loadAttrs()
    # stObj.setAttrs()
    # stObj.getAttrs()
    # 基于stObj的复杂操作了。
   
#def st2mem(stObj):
    # urlObj包含相关的网络信息，被直接拆解url路径了。生成核心数据。
    # stObj则包含文件系统的信息，同样会进行拆分了。生成核心数据。
    # metaObj，则包含文件系统的信息，利用上一层的特征数据，生成metaObj了。
    # 上一层的数据，会包含下层数据的钥匙。然后进入下层后进行转换了
    # 因此，每层其的数据，对于自己的不感兴趣，比如说md5.对于urlObj，stObj，memObj，都没有意义，只是一般的属性而已了。但是对于
    # md5Obj就不同了，所以md5层处于md5层了。是的。
    # md5层类，则附带有改层的信息了。是的。
    # return FMem(stObj.subject)


#def getStAttr(stObj):
    # memObj = st2mem(stObj)
    
    # return getData(memObj)

#def setStAttr(stObj,attrs):

    # memObj = st2mem(stObj)

    # attrs -> data
    # data = attrs2data
    # setData(memObj,data)    
    # data = getData(memObj)
    # attrs = data2attrs(data)

    # stObj.write(attrs)

# 陷入在了设计哲学中了。关于md5自身还带有meta？和实际的数据么？以及meta的读取如何？现在在st层上遇到问题了。是的。太过于复杂了。

# attrs 应该是md5所有的。这个之中，出现概念混乱了。st，是用户视图的。包括，meta和md5两层的内容。

# 底层好了，比如说md5ok了，那么上层就好了。是的。

# md5文件数据存在，那么文件才能存在了。否则不能存在。是的。

# FSt 类之对外提供事实，由上层业务进行判断了。

# 以'' 字符串生成的md5 不存在。exists为false

# 在stObj 和 md5Obj的关系中，需要md5Obj时，重新生成即可了。因为其的md5值是可能发生变化的。是的。

# 文件的判断，主要是md5了，md5文件在，则文件在，md5文件不在，则文件不在。meta为辅助，不重要。

# 关于dst，和lst，是如何使用的了？

# 前提一定是文件存在了。但是不能在setAttrs 函数中判断了。不判断业务，只执行。类中的函数，不需要思考。
