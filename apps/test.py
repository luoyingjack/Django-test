# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '202018/6/22 下午5:41' 
x = 177
def f(n):
    if n <= 3:
        a = n
    else:
        a = (n-1)+f(n-1)
    return a

b = f(x)
print(b)

def g(n):
    if n<=2:
        a=n
    else:
        a = f(n-1)+f(n-2)
    return a

print(f(x))