from django.db import models
from core.category.models import Category
from core.product.choices import um_choices
from django.forms import model_to_dict
from invpos.settings import MEDIA_URL, STATIC_URL
from datetime import datetime

class Product(models.Model):
    fechaent = models.DateField(verbose_name='Fecha de Entrada del Producto', default=datetime.now)
    factura = models.CharField(max_length=15, verbose_name='Factura de Entrada del Producto', default='Ninguna')
    codigo = models.CharField(max_length=15, verbose_name='Codigo del Producto', unique=True)
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Categoría')
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de venta')
    pcp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de costo')
    um = models.CharField(max_length=150, choices=um_choices, default='U', verbose_name='Unidad de Medidas',)
    stock = models.IntegerField(verbose_name='Cantidad Inicial', default=0)
    fechacad = models.DateField(verbose_name='Fecha de Vencimiento del Producto', default=datetime.now)
    stock_min = models.IntegerField(verbose_name='Stock Minimo', default=1)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['full_name']= '{} / {}'.format(self.name, self.cat.name) 
        item['cat'] = self.cat.toJSON()
        item['image'] = self.get_image()
        item['pvp'] = format(self.pvp, '.2f')
        return item

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']