# Generated by Django 3.2.8 on 2021-10-31 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kulder', '0013_alter_executive_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executive',
            name='experience',
            field=models.TextField(),
        ),
    ]
