# Generated by Django 3.2.8 on 2021-10-31 14:19

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Kulder', '0012_executive_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executive',
            name='experience',
            field=django_countries.fields.CountryField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
