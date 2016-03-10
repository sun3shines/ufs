

class Sets:

    def __init__(self):
        self.metadata = {}
        ## path , md5 会被作为metadata存储？？？
#        self.path = ''
#        self.md5 = ''
    def setMeta(self,key,value):
        self.metadata({key:value})

    def getMeta(self,key)
        return self.metadata.get(key)


