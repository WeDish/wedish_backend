from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)


class GenericProduct(models.Model):
    name = models.CharField(max_length=100)
    #allergen foreign key? example: nuts , eggs, milk, wheat, soy, seafood
    #type foreign key? example: vegan, vegetarian, meat, dairy, glutenfree...


class Service(models.Model):
    name = models.CharField(max_length=100)


class Unit(models.Model):
    name = models.CharField(max_length=100)
    # Type of Measurement: temperature, volume, weight


class Brand(models.Model):
    name = models.CharField(max_length=100)
    
class Allergen(models.Model):
    ALLERGEN_CATEGORIES = (
            (0, _("none")),
            (1, _("celery")),
            (2, _("cereals containing glutten")),
            (3, _("crustaceans")),
            (4, _("eggs")),
            (5, _("fish")),
            (6, _("lupin")),
            (7, _("milk")),
            (8, _("molluscs")),
            (9, _("mustard")),
            (10, _("peanuts")),
            (11, _("sesame")),
            (12, _("soybeans")),
            (13, _("sulphur dioxide and sulpites > 10 ppm")),
            (14, _("tree nuts")),
    )
    category = models.PositiveIntegerField(_('Allergen'), default=0, choices=ALLERGEN_CATEGORIES)
