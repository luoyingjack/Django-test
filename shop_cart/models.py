from django.db import models

# Create your models here.
from django.utils import timezone

'''
商品
'''
class Product(models.Model):
	title         = models.CharField(max_length=100, verbose_name="商品标题")
	description   = models.TextField(verbose_name="商品描述")
	image_url = models.ImageField(null=True, blank=True, upload_to="shopcart_ups/%Y/%m",
							  verbose_name="图片", max_length=200)
	price         = models.DecimalField(max_digits=8,decimal_places=2, verbose_name="价格")
	createtime = models.DateTimeField(default=timezone.now, db_index=True,
									  verbose_name="添加时间")

	def __str__(self):
		return self.title

	class Meta:
		db_table = "product"
		verbose_name = "商品信息"
		verbose_name_plural = verbose_name
		ordering = ["-createtime"]



'''
购物车中的条目
购物车中的条目与产品（Product）很 类似，
但是我们没有必要将这些信息再重复记录一次，而只需要让条目关联到产品即可。
条目中还会记录一些产品中没有的信息，比如数量
'''
class LineItem(models.Model):
	product = models.ForeignKey(Product)
	unit_price = models.DecimalField(max_digits=8,decimal_places=2)
	quantity = models.IntegerField()


	class Meta:
		db_table = "line_item"
		verbose_name = "条目"
		verbose_name_plural = verbose_name

'''
购物车
购物车是这些条目的容器。
购物车并不需要记录到数据库中，就好像超市并不关注顾客使用了哪些购物车而只关注他买了什么商品一样。
所以购物车不应该继承自models.Model，而仅仅应该是一个普通类
'''
class Cart(object):
	def __init__(self, *args, **kwargs):
		self.items = []
		self.total_price = 0

	def add_product(self, product):
		self.total_price += product.price

		for item in self.items:
			if item.product.id == product.id:
				item.quantity += 1
		return	self.items.append(LineItem(product=product,
											 unit_price=product.price,
											 quantity=1))




