from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name= 'nombre')
    price = models.IntegerField(verbose_name= 'precio')
    description = models.TextField(verbose_name= 'descripción')
    created = models.DateTimeField(auto_now_add=True, verbose_name= 'Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name= 'Fecha de modificación')

    class Meta:
        ordering =['name']