# Generated by Django 3.0.4 on 2020-03-31 21:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200401_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogposts',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 4, 1, 2, 58, 22, 728234)),
        ),
        migrations.AlterField(
            model_name='blogposts',
            name='title',
            field=models.TextField(),
        ),
    ]
