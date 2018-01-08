from django.db import models

# Create your models here.
class ProductsWarehouse(models.Model):
	"""docstring for ProductsWarehouse"""
	
	name = models.CharField(max_length =30, verbose_name = 'Товар')
	description = models.TextField(verbose_name = 'Описание')
	foto = models.URLField(verbose_name='Интернет-адрес')
	articals = models.IntegerField(default = 0,verbose_name='Код товара')
	price = models.IntegerField(default = 0,verbose_name='Цена товара')
	
	class Meta:
		verbose_name='Товар'
		verbose_name_plural='Товары'
			

	def __str__(self):
		return self.name

# cells	in the warehouse
class CellsWarehouse(models.Model):
	name = models.CharField(max_length =10,default = 0, verbose_name = 'Уровень')
	row_number = models.CharField(max_length =2, verbose_name = 'Ряд')
	cell = models.CharField(max_length =3, verbose_name = 'Ячейка')
	levelCell = models.CharField(max_length =3, verbose_name = 'Уровень')

	class Meta:
		verbose_name = 'Ячейка'
		verbose_name_plural = 'Ячейки'

	def __str__(self):
		return self.name
	
    
class Storage(models.Model):
	name = models.CharField(max_length =10,default = 0, verbose_name = 'Место хранения')
	cellsWarehouse = models.ForeignKey('CellsWarehouse', models.SET_NULL, blank=True, null=True,)
	productsWarehouse = models.ForeignKey('ProductsWarehouse', models.SET_NULL, blank=True, null=True,)
	number = models.IntegerField(default = 0,verbose_name='Количество')

	class Meta:
		verbose_name = 'Место хранения'
		verbose_name_plural = 'Места хранения'

	def __str__(self):
		return self.name


						