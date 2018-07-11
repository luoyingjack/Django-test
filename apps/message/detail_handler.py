# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render
from apps.message.models import Art


__author__ = 'jack'
__date__ = '2018/6/20 20:20'

def DetailHandler(request):
   print('DetailHandler#enter!')
   #id = self.get_argument("id", None)
   id = request.GET.get("id", None)
   print('DetailHandler#id:' + str(id))
   if id == None:
      return HttpResponseRedirect("/message/index/")
   else:
      art = Art.objects.get(id=int(id))
      context = {"art":art}
      return render(request, "home/detail.html", context=context)