# Generated by Django 3.0.4 on 2020-04-15 08:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeportal', '0043_auto_20200415_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem_statements',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 15, 14, 26, 47, 443521)),
        ),
    ]
