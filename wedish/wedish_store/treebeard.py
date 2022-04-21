from wedish_backend.wedish.wedish_store.models import Category


tree_data = [{'plot':{'name':'Category'}, 'children':[
            {'plot':{'name':'Product'}, 'children':[
                {'plot':{'name':'Meal'}, 'children':[
                    {'plot':{'name':'Breakfast'}},
                    {'plot':{'name':'Brunch'}},
                    {'plot':{'name':'Lunch'}},
                    {'plot':{'name':'Hi-Tea'}},
                    {'plot':{'name':'Dinner'}},
                    {'plot':{'name':'Supper'}},
                    ]},
                {'plot':{'name':'Drink'}, 'children':[
                    {'plot':{'name':'Soft drinks'}},
                    {'plot':{'name':'Coctail'}},
                    {'plot':{'name':'Alcohol'}},
                    {'plot':{'name':'Alcohol coktail'}},
                    {'plot':{'name':'Tea'}},
                    {'plot':{'name':'Coffee'}},
                    ]},
                {'plot':{'name':'Other'}},
                ]},
            {'plot':{'name':'Service'}, 'children':[
                {'plot':{'name':'Place to eat'}},
                {'plot':{'name':'Take out'}},
                ]},
            {'plot':{'name':'General_Product'}, 'children':[
                {'plot':{'name':'Grains'}},
                {'plot':{'name':'Vegetable'}},
                {'plot':{'name':'Fruits'}},
                {'plot':{'name':'Meat'}},
                {'plot':{'name':'Liquids'}},
                {'plot':{'name':'Spices'}},
                {'plot':{'name':'Eggs, milk...'}},
                 ]},
            {'plot':{'name':'Brand'}},
            {'plot':{'name':'Unit'},  'children':[
                {'plot':{'name':'Weight'}},
                {'plot':{'name':'Temperature'}},
                {'plot':{'name':'Data'}},
                {'plot':{'name':'Time'}},
                {'plot':{'name':'Lenght'}},
                {'plot':{'name':'Currency'}},
                ]}, 
            ]},
]

Category.load_bulk(tree_data, None)