# Generated by Django 4.0.4 on 2022-05-12 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedish_recipy', '0007_alter_good_picture'),
        ('wedish_accounting', '0004_companyname'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CompanyName',
            new_name='Company',
        ),
    ]
