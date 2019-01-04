from django.db import models
from materials.models import AddAndCreate, Product, Material

def get_upload_realization_path(self, filename):
        return os.path.join("photos/{}/{}".format(self.used_wood, self.location), filename)

class Ralization(AddAndCreate):
    name = models.CharField('Tytuł realizacji', max_length=100)
    cost = models.DecimalField('Koszt realizacji (PLN)', max_digits=5, decimal_places=2)
    location = models.CharField('Lokalizacja', max_length=100)
    description = models.TextField('Opis realizacji', blank=True)
    used_wood = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name='Użyte drewno')
    used_joist = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name='Użyte legary', null=True, blank=True)
    other_products = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name='Inne produkty', null=True, blank=True)
    used_materials1 = models.ForeignKey(Material, on_delete=models.DO_NOTHING, verbose_name='Użyte materiały (1)', null=True, blank=True)
    used_materials1 = models.ForeignKey(Material, on_delete=models.DO_NOTHING, verbose_name='Użyte materiały (2)', null=True, blank=True)
    used_materials1 = models.ForeignKey(Material, on_delete=models.DO_NOTHING, verbose_name='Użyte materiały (3)', null=True, blank=True)
    photo_main = models.ImageField('Obraz gółwny', upload_to=get_upload_path)
    photo_2 = models.ImageField('Obraz 2', upload_to=get_upload_path, blank=True)
    photo_3 = models.ImageField('Obraz 3', upload_to=get_upload_path, blank=True)
    photo_4 = models.ImageField('Obraz 4', upload_to=get_upload_path, blank=True)
    photo_5 = models.ImageField('Obraz 5', upload_to=get_upload_path, blank=True)