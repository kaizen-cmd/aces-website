# Generated by Django 3.0.4 on 2020-04-14 12:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200414_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogposts',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 4, 14, 18, 18, 34, 40820)),
        ),
    ]
