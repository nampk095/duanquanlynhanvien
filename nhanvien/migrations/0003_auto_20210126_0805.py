# Generated by Django 3.1.5 on 2021-01-26 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nhanvien', '0002_auto_20210126_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nhanvien',
            name='econtact',
            field=models.CharField(max_length=300),
        ),
    ]
