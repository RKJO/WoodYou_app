from django.db import models
from materials.models import AddAndCreate

class Assembly(AddAndCreate):
    assembly_typ = models.CharField('Typ zabudowy', max_length=100)        price_m2 = models.DecimalField(verbose_name=u'Cena m² (PLN)', max_digits=5, decimal_places=2)
    description = models.TextField('Opis produktu', blank=True)

    class Meta:
        verbose_name = "Montaż"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
