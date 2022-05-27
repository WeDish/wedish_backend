# Generated by Django 4.0.4 on 2022-04-26 15:56

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='name')),
                ('picture', models.ImageField(default='wedish_store/img/default_brand.png', upload_to='', verbose_name='picture')),
                ('description', tinymce.models.HTMLField(blank=True, default='', max_length=10000, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GenericProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'generic product',
                'verbose_name_plural': 'generic products',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Name')),
                ('unit_category', models.CharField(choices=[('kg', 'kilograms'), ('L', 'liters'), ('pcs', 'units')], db_index=True, max_length=7)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='wedish_store.brand', verbose_name='Brand')),
                ('generic_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='wedish_store.genericproduct', verbose_name='Generic Product')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductAllergen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Name')),
                ('allergen_category', models.CharField(choices=[('none', 'none'), ('celery', 'celery'), ('glutten', 'cereals containing glutten'), ('crustaceans', 'crustaceans'), ('eggs', 'eggs'), ('fish', 'fish'), ('lupin', 'lupin'), ('milk', 'milk'), ('molluscs', 'molluscs'), ('mustard', 'mustard'), ('peanuts', 'peanuts'), ('sesame', 'sesame'), ('soybeans', 'soybeans'), ('SO', 'sulphur dioxide and sulpites > 10 ppm'), ('tree nuts', 'tree nuts')], db_index=True, max_length=63)),
                ('generic_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allergens', to='wedish_store.genericproduct', verbose_name='Generic Product')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allergens', to='wedish_store.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product Allergen',
                'verbose_name_plural': 'Product Allergen',
            },
        ),
    ]
    