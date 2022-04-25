# Generated by Django 4.0.4 on 2022-04-25 18:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wedish_recipy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('priority_index', models.IntegerField(default=0)),
                ('name', models.CharField(help_text='ex.: Salad, Roast, Pizza...', max_length=63, verbose_name='name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='ex.: Day menu, Festive menu, Ordinary menu', max_length=30, verbose_name='name')),
                ('valid_from', models.DateField(blank=True, db_index=True, default=django.utils.timezone.now, null=True, verbose_name='valid from')),
                ('valid_until', models.DateField(blank=True, db_index=True, null=True, verbose_name='valid until')),
                ('publicity', models.PositiveIntegerField(choices=[(0, 'Public'), (1, 'Private')], default=1, verbose_name='publicity')),
            ],
            options={
                'verbose_name': 'menu',
                'verbose_name_plural': 'menus',
                'ordering': ['name', 'valid_from'],
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority_index', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=63, verbose_name='name')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='price')),
                ('category_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wedish_menu.category', verbose_name='category group')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wedish_recipy.good', verbose_name='item')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wedish_menu.menu', verbose_name='menu'),
        ),
    ]
