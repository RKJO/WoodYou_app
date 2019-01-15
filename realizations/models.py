from django.db import models
from materials.models import Product, Material
from calculations.models import Assembly
from categories.models import AddAndCreate, RealizationCategory
import os

def get_upload_realization_path(self, filename):
        return os.path.join("photos/{}/{}".format(self.used_wood, self.location), filename)

class Ralization(AddAndCreate):
    category_name = models.ManyToManyField(RealizationCategory, verbose_name='Kategoria')
    name = models.CharField('Tytuł realizacji', max_length=100)
    cost = models.IntegerField('Koszt realizacji (PLN)')
    area = models.DecimalField(verbose_name=u'Powierzchnia m²', max_digits=8, decimal_places=1)
    location = models.CharField('Lokalizacja', max_length=100)
    description = models.TextField('Opis realizacji', blank=True)
    realization_time = models.IntegerField('Czas realizacji (dni)')
    realization_date = models.DateField(verbose_name='Termin realizacji')
    used_wood = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name='Użyte drewno', related_name='used_wood')
    used_products1 = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name='Użyte produkty (1)', related_name='used_products1', null=True, blank=True)
    used_products2 = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name='Użyte produkty (2)', related_name='used_products2',null=True, blank=True)
    used_materials1 = models.ForeignKey(Material, on_delete=models.DO_NOTHING, verbose_name='Użyte materiały (1)', related_name='used_materials1', null=True, blank=True)
    used_materials2 = models.ForeignKey(Material, on_delete=models.DO_NOTHING, verbose_name='Użyte materiały (2)', related_name='used_materials2', null=True, blank=True)
    used_materials3 = models.ForeignKey(Material, on_delete=models.DO_NOTHING, verbose_name='Użyte materiały (3)', related_name='used_materials3', null=True, blank=True)
    assembly_type = models.ForeignKey(Assembly, on_delete=models.DO_NOTHING, verbose_name='Typ zabudowy', null=True, blank=True)
    photo_main = models.ImageField('Obraz gółwny', upload_to=get_upload_realization_path)
    photo_2 = models.ImageField('Obraz 2', upload_to=get_upload_realization_path, blank=True)
    photo_3 = models.ImageField('Obraz 3', upload_to=get_upload_realization_path, blank=True)
    photo_4 = models.ImageField('Obraz 4', upload_to=get_upload_realization_path, blank=True)
    photo_5 = models.ImageField('Obraz 5', upload_to=get_upload_realization_path, blank=True)

    class Meta:
        verbose_name = "Realizacja"
        verbose_name_plural = "Realizacje"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
