# Generated by Django 3.0.4 on 2020-04-25 15:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0004_auto_20200425_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='username',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
    ]
