# Generated by Django 3.2.13 on 2022-06-01 17:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_tutorial_tutorial_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 1, 17, 3, 23, 169748), verbose_name='date published'),
        ),
    ]
