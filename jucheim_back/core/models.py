from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категория'

    name = models.CharField(max_length=1000, verbose_name='Наименование')

class Products(models.Model):
    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукт'

    name = models.CharField(max_length=1000, verbose_name='Наименование')
    price = models.FloatField(verbose_name='Цена')
    category = models.ForeignKey(Category, related_name="category_product", null=True,
                                    on_delete=models.SET_NULL,help_text=("Категория продукта"))
    photo = models.ImageField(upload_to='products', null = True)
    description = models.TextField(null = True)


class PhotoProducts(models.Model):
    class Meta:
        verbose_name = 'Фото продутков'
        verbose_name_plural = 'Фото продутков'

    product = models.ForeignKey(Products, related_name="photo_product", null=True,
                                    on_delete=models.SET_NULL,help_text=("Фото продукта"))
    photo = models.ImageField(upload_to='photosproduct', null = True)


class Banners(models.Model):
    class Meta:
        verbose_name = 'Банеры'
        verbose_name_plural = 'Банер'

    product = models.ForeignKey(Products, related_name="banner_product", null=True,
                                    on_delete=models.SET_NULL,help_text=("Продукта"))
    category = models.ForeignKey(Category, related_name="banner_category", null=True,
                                    on_delete=models.SET_NULL,help_text=("Категория продукта"))
    photo_banner = models.ImageField(upload_to='banners', null = True)
   
    
