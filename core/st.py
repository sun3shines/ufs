

class FSt:
    def __ini__(self,subject):
        self.subject = subject
        self.prefix = '/mnt/storage/'

    def getPath():
        return self.subject+self.prefix

    def initSt():
        # 采集文件系统级别的数据，用户，大小。chmod，权限等。
        pass
        
def st2mem(stObj):
    # urlObj包含相关的网络信息，被直接拆解url路径了。生成核心数据。
    # stObj则包含文件系统的信息，同样会进行拆分了。生成核心数据。
    # metaObj，则包含文件系统的信息，利用上一层的特征数据，生成metaObj了。
    # 上一层的数据，会包含下层数据的钥匙。然后进入下层后进行转换了
    # 因此，每层其的数据，对于自己的不感兴趣，比如说md5.对于urlObj，stObj，memObj，都没有意义，只是一般的属性而已了。但是对于
    # md5Obj就不同了，所以md5层处于md5层了。是的。
    # md5层类，则附带有改层的信息了。是的。
    return FMem(stObj.subject)


def getStAttr(stObj):
    memObj = st2mem(stObj)
    return getData(memObj)
    
