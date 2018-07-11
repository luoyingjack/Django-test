from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from shop_cart.models import Product, Cart
import datetime

def IndexHandler(request):
	products = Product.objects.all()
	context = dict(
       products = products
	)
	return render(request, "store.html", context=context)


'''
查看购物车
'''
def ViewCartHandler(request):
	cart = request.session.get("cart", None)
	#t = get_template('depotapp/view_cart.html')
	if not cart:
		cart = Cart()
	request.session["cart"] = cart
	context = dict(
		cart = cart
	)
	return render(request, "view_cart.html", context=context)


'''
加入购物车
'''
def AddCartHandler(request, id):
	product = Product.objects.get(id=id)
	cart = request.session.get("cart", None)
	if not cart:
		cart = Cart()
		request.session["cart"] = cart
	else:
		cart.add_product(product)
		request.session['cart'] = cart
	return ViewCartHandler(request)



'''
清空购物车
'''
def CleanCartHandler(request):
	del request.session['cart']
	return ViewCartHandler(request)