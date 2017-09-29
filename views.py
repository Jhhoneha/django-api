# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def index(request):
    #写着这个页面的业务逻辑，然后再返回
     #return HttpResponse('Hello World!!!')
     return render(request,'index.html')

def upload(request):
    if request.method == 'POST':
        myfile = request.FILES.get('file')
        if not myfile:
              return JsonResponse({'result':1000,'success':False,'msg':'必须选择文件再上传'})
        filename = myfile.name
        file = myfile.read()
        filesize = myfile.size
        if filesize == 0:
            return JsonResponse({'result':1001,'success':False,'msg':'不能传空文件'})

        with open('upload/%s' %filename,'wb') as fn:
            fn.write(file)

        return JsonResponse({'result':200,'success':True,'msg':'','path':'http:/127.0.0.1:8000/upload/%s' %filename})
    return JsonResponse({'result':405,'success':False,'msg':'不被允许'})

def download(request,filename):
    file = open('upload/%s' %filename).read()
    response = HttpResponse(file)
    response['Content-type'] = "application/octet-stream"
    response['Content-Disposition'] = 'attachment:filename=%s'
    return HttpResponse(file)

