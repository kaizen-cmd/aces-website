# Generated by Django 3.0.4 on 2020-04-14 11:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeportal', '0024_auto_20200414_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem_statements',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 14, 16, 39, 52, 926895)),
        ),
    ]
