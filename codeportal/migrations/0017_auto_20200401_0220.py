# Generated by Django 3.0.4 on 2020-03-31 20:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeportal', '0016_auto_20200331_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem_statements',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 1, 2, 20, 29, 19148)),
        ),
    ]
