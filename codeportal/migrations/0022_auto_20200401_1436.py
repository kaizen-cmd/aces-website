# Generated by Django 3.0.4 on 2020-04-01 09:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeportal', '0021_auto_20200401_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem_statements',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 1, 14, 36, 2, 735739)),
        ),
    ]
