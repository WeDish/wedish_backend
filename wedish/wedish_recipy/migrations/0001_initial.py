# Generated by Django 4.0.4 on 2022-04-20 15:18

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='name')),
                ('category', models.PositiveIntegerField(choices=[(0, 'dish'), (1, 'drink')], default=0, verbose_name='Status')),
                ('recommended_retail_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='recommended retail price')),
                ('picture', models.ImageField(default='wedish_recipy/img/default.jpg', upload_to='', verbose_name='picture')),
                ('description', tinymce.models.HTMLField(blank=True, default='', max_length=10000, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]