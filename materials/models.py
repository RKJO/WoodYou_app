from django.db import models
from datetime import date


class AddAndCreate(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def get_date(self):
        return self.created_at, self.created_at

    class Meta:
        abstract = True


class Category(AddAndCreate):
    name = models.CharField('Nazwa Kategorii', max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Kategoria"

    def __unicode__(self):
        return self.name


class Product(AddAndCreate):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField('Nazwa produktu', max_length=100)
    price_lm = models.DecimalField('Cena mb (PLN)', max_digits=5, decimal_places=2)
    price_m2 = models.DecimalField('Cena m^2 (PLN)', max_digits=5, decimal_places=2)
    thickness = models.IntegerField('Gruboość (mm)')
    width = models.IntegerField('Szerokość (mm)')
    weight = models.DecimalField('Waga', max_digits=5, decimal_places=2)
    material = models.CharField('Materiał', max_length=100)
    kind = models.CharField('Gatunek', max_length=10, blank=True)
    description = models.TextField(blank=True)
    photo_main = models.ImageField('Obraz gółwny', upload_to='photos/%Y/%m/%d/')
    photo_2 = models.ImageField('Obraz 2', upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField('Obraz 3', upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField('Obraz 4', upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField('Obraz 5', upload_to='photos/%Y/%m/%d/', blank=True)

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"

    def __unicode__(self):
        return self.name


class Material(AddAndCreate):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField('Nazwa Materiału', max_length=120)
    price = models.DecimalField('Cena (PLN)', max_digits=5, decimal_places=2)
    description = models.TextField('Opis Materiału', blank=True)
    photo_main = models.ImageField('Obraz gółwny', upload_to='photos/%Y/%m/%d/')
    photo_2 = models.ImageField('Obraz 2', upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField('Obraz 3', upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField('Obraz 4', upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField('Obraz 5', upload_to='photos/%Y/%m/%d/', blank=True)

    class Meta:
        verbose_name = "Materiał"
        verbose_name_plural = "Materiały"

    def __unicode__(self):
        return self.name