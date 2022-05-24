# Generated by Django 4.0.4 on 2022-05-09 16:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wedish_recipy', '0005_alter_vat_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vat',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='vat',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='start date'),
        ),
    ]
