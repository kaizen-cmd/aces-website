# Generated by Django 3.0.4 on 2020-03-28 19:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeportal', '0008_auto_20200329_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem_statements',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2020, 3, 29, 1, 19, 13, 405667)),
        ),
        migrations.AlterField(
            model_name='submission',
            name='check',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='submission',
            name='contestant',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='submission',
            name='probstatement',
            field=models.TextField(max_length=100),
        ),
    ]
