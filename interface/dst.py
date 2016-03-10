# -*- coding: utf-8 -*-

import os
import os.path

class DSt:

    def __init__(self,subject):
        self.prefix = '/mnt/storage/'
        self.subject = subject
    pass

    @property
    def path(self):
        return self.prefix + self.subject

    @property
    def exists(self):
        if os.path.exists(self.path):
            return True
        return False

    def put(self):
        os.mkdir(self.path)

    def list(self,r=False):
        # 若为文件，则获取到文件的内容了。若为dir，则获取到目录的内容。
        return []

    def delete(self,r=False):

        if r:
            shutil.rmtree(self.path)
        else:
            try:
                os.rmdir(self.path)
            except:
                return 409

        return 204

    def copy(self,d):
        try:
            shutil.copytree(self.path,d.path,symlinks=True) 
            return 200
        except:
            return 400

    def move(self,d)
        shutil.move(self.path,d.path) 

if __name__ == '__main__':
    pass

# DSt 类完全是文件系统级别上的任务了。文件读取，属性读取等。

# url 层的req的处理。然后转化为了实际的dir对象了。文件系统对象来处理了。但是dst要稍微复杂点，所以层次会多了。是的。

# 从网络对象，转化为文件对象了。但是还是要管理很多的fst对象的？是的。以及目录下有目录，这些又该如何设计？更好？

# 这个就是文件系统的能力，和抽象层次的能力的区别了。是的。 #　这个时候就是管理对象的问题了。干脆就是完全的直接文件系统解析吧。而绕过业务了。结果直接从文件系统中获取了。把矛盾留给文件系统级别来解决了。

# 从文件系统级别来返回错误码了，不可让高层的业务伸手进入文件系统级别了。等于是这样的，即我们把高层次的矛盾，通过接口，交给了低层次，但是高层次不对底层解决问题的方式有太多的干涉了。

# 如何对于底层的内容给出一个合理的封装？ g给出初始化的参数了？就可以了？然后就不要干涉了。比如说path是进入fs的方式了。是的。
