# -*- coding: utf-8 -*-

from cloudcommon.common.bufferedhttp import jresponse

url2view = {}

strFilePut = '/file/put'
url2view.update({strFilePut:None})

strFileGet = '/file/get'
url2view.update({strFileGet:None})

strFileDelete = '/file/delete'
url2view.update({strFileDelete:None})

strFileHead = '/file/head'
url2view.update({strFileHead,None})

strFilePost = '/file/post'
url2view.update({strFilePost:None})

strFileMove = '/file/move'
url2view.update({strFileMove:None})

strFileCopy = '/file/copy'
url2view.update({strFileCopy:None})

strDirPut = '/dir/put'
url2view.update({strDirPut:None})

strDirGet = '/dir/get'
url2view.update({strDirGet:None})

strDirDelete = '/dir/delete'
url2view.update({strDirDelete:None})

strDirCopy = '/dir/copy'
url2view.update({strDirCopy:None})

strDirMove = '/dir/move'
url2view.update({strDirMove:None})

def handlerequest(req,sdata):
    
    url = req.path
    if url not in url2view:
        return jresponse('-1','url error',req,404)
    return url2view[url](req,sdata)

