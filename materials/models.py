from django.db import models
from datetime import date
import os
from categories.models import AddAndCreate, ProductCategory, MaterialCategory

def get_upload_path(self, filename):
        return os.path.join("photos/{}/{}".format(self.category_name, self.name), filename)

class Product(AddAndCreate):
    category_name = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Kategoria')
    name = models.CharField('Nazwa produktu', max_length=100)
    price_lm = models.DecimalField('Cena mb (PLN)', max_digits=5, decimal_places=2)
    price_m2 = models.DecimalField(verbose_name=u'Cena m² (PLN)', max_digits=5, decimal_places=2)
    thickness = models.IntegerField('Gruboość (mm)')
    width = models.IntegerField('Szerokość (mm)')
    weight = models.DecimalField('Waga', max_digits=5, decimal_places=2, blank=True, null=True)
    material = models.CharField('Materiał', max_length=100)
    kind = models.CharField('Gatunek', max_length=100, blank=True)
    description = models.TextField('Opis produktu', blank=True)
    used_for_calculate = models.BooleanField('Pokaż w kalkulatorze', default=True)
    photo_main = models.ImageField('Obraz gółwny', upload_to=get_upload_path)
    photo_2 = models.ImageField('Obraz 2', upload_to=get_upload_path, blank=True)
    photo_3 = models.ImageField('Obraz 3', upload_to=get_upload_path, blank=True)
    photo_4 = models.ImageField('Obraz 4', upload_to=get_upload_path, blank=True)
    photo_5 = models.ImageField('Obraz 5', upload_to=get_upload_path, blank=True)

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Material(AddAndCreate):
    category_name = models.ForeignKey(MaterialCategory, on_delete=models.CASCADE, verbose_name='Kategoria')
    name = models.CharField('Nazwa Materiału', max_length=120)
    price = models.DecimalField('Cena (PLN)', max_digits=5, decimal_places=2)
    description = models.TextField('Opis Materiału', blank=True)
    photo_main = models.ImageField('Obraz gółwny', upload_to=get_upload_path)
    photo_2 = models.ImageField('Obraz 2', upload_to=get_upload_path, blank=True)
    photo_3 = models.ImageField('Obraz 3', upload_to=get_upload_path, blank=True)
    photo_4 = models.ImageField('Obraz 4', upload_to=get_upload_path, blank=True)
    photo_5 = models.ImageField('Obraz 5', upload_to=get_upload_path, blank=True)

    class Meta:
        verbose_name = "Akcesoria"
        verbose_name_plural = "Akcesoria"
    
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name