from django.db import models
from treebeard.mp_tree import MP_Node


class Product(models.Model):
    name = models.CharField(max_length=100)


class GenericProduct(models.Model):
    name = models.CharField(max_length=100)
    # allergen foreign key? example: nuts , eggs, milk, wheat, soy, seafood
    # type foreign key? example: vegan, vegetarian, meat, dairy, glutenfree...


class Service(models.Model):
    name = models.CharField(max_length=100)


class Unit(models.Model):
    name = models.CharField(max_length=100)
    # Type of Measurement: temperature, volume, weight


class Brand(models.Model):
    name = models.CharField(max_length=100)


class Category(MP_Node):
    name = models.CharField(max_length=100)
    node_order_by = ['name']

    def __str__(self):
        return 'Category: {}'.format(self.name)
