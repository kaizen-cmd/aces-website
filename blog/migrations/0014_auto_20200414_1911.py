# Generated by Django 3.0.4 on 2020-04-14 13:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200414_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogposts',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 4, 14, 19, 11, 4, 389463)),
        ),
    ]
