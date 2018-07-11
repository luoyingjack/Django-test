# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '202018/6/21 上午9:43' 

from  django.shortcuts import render, HttpResponseRedirect
from .models import Tag, Art



'''
详情页面功能：
      接口URL：  /art/detail?id=7
      方法：GET
      输入参数说明：
          id： 文章id，（点击某一个具体的文章，传入文章id)

     输出： 渲染详情页面
'''
def DetailHandler(request):
	art_id = int(request.GET.get('id', 0))
	if art_id == 0:
		return HttpResponseRedirect('/art/index')
	else:
		art_inst = Art.objects.get(id = art_id)
		context = dict(
			art = art_inst
		)
		return render(request, "home/detail_handler.html", context=context)