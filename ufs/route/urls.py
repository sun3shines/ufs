# -*- coding: utf-8 -*-

from cloudcommon.common.bufferedhttp import jresponse
import ufs.interface.fviews
import ufs.interface.dviews
import ufs.interface.cviews

url2view = {}

strFilePut = '/file/put'
url2view.update({strFilePut:ufs.interface.fviews.put})

strFileGet = '/file/get'
url2view.update({strFileGet:ufs.interface.fviews.get})

strFileDelete = '/file/delete'
url2view.update({strFileDelete:ufs.interface.fviews.delete})

strFileHead = '/file/head'
url2view.update({strFileHead,ufs.interface.fviews.head})

strFilePost = '/file/post'
url2view.update({strFilePost:ufs.interface.fviews.post})

strFileMove = '/file/move'
url2view.update({strFileMove:ufs.interface.fviews.move})

strFileCopy = '/file/copy'
url2view.update({strFileCopy:ufs.interface.fviews.copy})

strDirPut = '/dir/put'
url2view.update({strDirPut:ufs.interface.dviews.put})

strDirGet = '/dir/get'
url2view.update({strDirGet:ufs.interface.dviews.get})

strDirDelete = '/dir/delete'
url2view.update({strDirDelete:ufs.interface.dviews.delete})

strDirCopy = '/dir/copy'
url2view.update({strDirCopy:ufs.interface.dviews.copy})

strDirMove = '/dir/move'
url2view.update({strDirMove:ufs.interface.dviews.move})

strContainerPut = '/container/put'
url2view.update({strContainerPut:ufs.interface.cviews.put})

strContainerGet = '/container/get'
url2view.update({strContainerGet:ufs.interface.cviews.get})

strContainerDelete = '/container/delete'
url2view.update({strContainerDelete:ufs.interface.cviews.delete})

strContainerHead = '/container/head'
url2view.update({strContainerHead:ufs.interface.cviews.head})

strContainerPost = '/container/post'
url2view.update({strContainerPost:ufs.interface.cviews.post})

def handlerequest(req,sdata):
    
    url = req.path
    if url not in url2view:
        return jresponse('-1','url error',req,404)
    return url2view[url](req,sdata)

