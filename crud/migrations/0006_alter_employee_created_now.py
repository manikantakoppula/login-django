# Generated by Django 4.1.7 on 2023-03-21 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_alter_employee_created_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='created_now',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 21, 15, 7, 16, 287574)),
        ),
    ]
