# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '202018/6/24 下午5:41' 

from django.conf.urls import url
from shop_cart.views import IndexHandler, ViewCartHandler, AddCartHandler, CleanCartHandler

'''
二级路由入口文件
'''

urlpatterns = [
	url(r'^$', IndexHandler),
	url(r'^cart/view/$', ViewCartHandler),
	url(r'cart/view/(?P<id>[^/]+)/$', AddCartHandler),
	url(r'cart/clean/$', CleanCartHandler),
]