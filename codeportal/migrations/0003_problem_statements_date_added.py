# Generated by Django 3.0.4 on 2020-03-28 08:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeportal', '0002_problem_statements_test_case'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem_statements',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2020, 3, 28, 14, 8, 36, 194140)),
        ),
    ]
