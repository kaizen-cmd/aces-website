# Generated by Django 3.0.4 on 2020-04-14 21:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeportal', '0032_auto_20200415_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem_statements',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 15, 2, 57, 53, 253916)),
        ),
    ]
