# Generated by Django 4.0.4 on 2022-05-05 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedish_recipy', '0004_country_region_vat_subregion_good_vat_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vat',
            name='rate',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=10, null=True, verbose_name='rate'),
        ),
    ]
