# Generated by Django 3.0.4 on 2020-04-15 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aces', '0010_auto_20200415_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepagecontent',
            name='mentors',
        ),
    ]
