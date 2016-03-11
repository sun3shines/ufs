# -*- coding: utf-8 -*-

import json
import os
import os.path

class Meta:

    def __init__(self,path):
        self.path = path

    def put(self,attrs):
        
        with file(self.path,'w') as f:
            json.dump(attrs,f) 

    def get(self):
        with open(self.path) as f:
            attrs = json.load(f)
            return attrs

    def delete(self):
        os.remove(self.path)

# 关于Meta对象，和Md5对象相似，需要的时候创建即可了。主要是作为数据的存储了。而不过多的基于其他的判断了。比如说exists，这个是不需要的。

# 涉及数据的流动了。数据需要修改的时候创建了。
