# Generated by Django 3.2.13 on 2022-06-01 16:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_tutorial_tutorial_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 1, 16, 30, 52, 155251), verbose_name='date published'),
        ),
    ]
