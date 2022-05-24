# Generated by Django 4.0.4 on 2022-05-12 16:02

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    replaces = [('wedish_accounting', '0004_companyname'), ('wedish_accounting', '0005_rename_companyname_company')]

    dependencies = [
        ('wedish_recipy', '0007_alter_good_picture'),
        ('wedish_accounting', '0003_alter_region_unique_together_remove_region_country_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='company name')),
                ('business_id', models.DecimalField(decimal_places=0, help_text='company id', max_digits=20, unique=True, verbose_name='business id')),
                ('VAT_id', models.CharField(db_index=True, max_length=12, unique=True, verbose_name='VAT id')),
                ('IBAN', models.CharField(blank=True, db_index=True, max_length=34, null=True, verbose_name='IBAN')),
                ('BIC', models.CharField(blank=True, max_length=11, null=True, verbose_name='BIC')),
                ('address', models.CharField(max_length=200, verbose_name='address')),
                ('email', models.EmailField(blank=True, max_length=150, null=True, verbose_name='email')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='phone number')),
                ('is_owner', models.BooleanField(default=False, verbose_name='is owner')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wedish_recipy.country')),
            ],
        ),
    ]