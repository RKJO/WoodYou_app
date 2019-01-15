from django.db import models

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
        abstract = True

class ProductCategory(Category):
    type_choice = {
        (1, 'Deski'),
        (2, 'Drewno Konstrukcyjne'),
        (3, 'Inne'),
    }

    product_type = models.IntegerField('Typ', choices=type_choice)

    class Meta:
        verbose_name = "Kategoria Produktu"
        verbose_name_plural = "Kategorie Produktów"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class MaterialCategory(Category):

    class Meta:
        verbose_name = "Kategoria Materiału"
        verbose_name_plural = "Kategorie Materiałów"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class RealizationCategory(Category):

    class Meta:
        verbose_name = "Kategoria Realizacji"
        verbose_name_plural = "Kategorie Realizacji"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
