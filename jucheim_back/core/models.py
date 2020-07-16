from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категория'

    name = models.CharField(max_length=1000, verbose_name='Наименование')
    
