# Generated by Django 4.0.4 on 2022-05-10 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedish_recipy', '0006_alter_vat_end_date_alter_vat_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='picture',
            field=models.ImageField(default='wedish_recipy/goods/default.jpg', upload_to='wedish_recipy/goods', verbose_name='picture'),
        ),
    ]
