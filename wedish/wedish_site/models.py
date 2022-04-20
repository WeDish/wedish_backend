from django.db import models
from treebeard.mp_tree import MP_Node



# Create your models here.


class Category(MP_Node):
    name = models.CharField(max_length=100)
    node_order_by = ['name']

    def __str__(self):
        return 'Category: {}'.format(self.name)


data = [{'data':{'name':'Category'}, 'children':[
            {'data':{'name':'Product'}, 'children':[
                {'data':{'name':'Meal'}, 'children':[
                    {'data':{'name':'Breakfast'}},
                    {'data':{'name':'Brunch'}},
                    {'data':{'name':'Lunch'}},
                    {'data':{'name':'Hi-Tea'}},
                    {'data':{'name':'Dinner'}},
                    {'data':{'name':'Supper'}},
                    ]},
                {'data':{'name':'Drink'}, 'children':[
                    {'data':{'name':'Soft drinks'}},
                    {'data':{'name':'Coctail'}},
                    {'data':{'name':'Alcohol'}},
                    {'data':{'name':'Alcohol coktail'}},
                    {'data':{'name':'Tea'}},
                    {'data':{'name':'Coffee'}},
                    ]},
                {'data':{'name':'Other'}},
                ]},
            {'data':{'name':'Service'}, 'children':[
                {'data':{'name':'Place to eat'}},
                {'data':{'name':'Take out'}},
                ]},
            {'data':{'name':'General_Product'}, 'children':[
                {'data':{'name':'Grains'}},
                {'data':{'name':'Vegetable'}},
                {'data':{'name':'Fruits'}},
                {'data':{'name':'Meat'}},
                {'data':{'name':'Liquids'}},
                {'data':{'name':'Spices'}},
                {'data':{'name':'Eggs, milk...'}},
                 ]},
            {'data':{'name':'Brand'}},
            {'data':{'name':'Unit'},  'children':[
                {'data':{'name':'Weight'}},
                {'data':{'name':'Temperature'}},
                {'data':{'name':'Data'}},
                {'data':{'name':'Time'}},
                {'data':{'name':'Lenght'}},
                {'data':{'name':'Currency'}},
                ]}, 
            ]},
]