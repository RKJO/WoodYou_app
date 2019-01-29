from django.db import models
from materials.models import AddAndCreate

class Assembly(AddAndCreate):
    assembly_type = models.CharField('Typ zabudowy', max_length=100)
    price_m2 = models.DecimalField(verbose_name=u'Cena m² (PLN)', max_digits=5, decimal_places=2)
    description = models.TextField('Opis produktu', blank=True)

    class Meta:
        verbose_name = "Typ montażu"
        verbose_name_plural = "Typy montażu"


    def __str__(self):
        return self.assembly_type

    def __unicode__(self):
        return self.assembly_type
