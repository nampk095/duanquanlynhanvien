# Generated by Django 3.1.5 on 2021-01-26 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nhanvien', '0003_auto_20210126_0805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nhanvien',
            old_name='econtact',
            new_name='nvcontact',
        ),
        migrations.RenameField(
            model_name='nhanvien',
            old_name='eemail',
            new_name='nvemail',
        ),
        migrations.RenameField(
            model_name='nhanvien',
            old_name='eid',
            new_name='nvid',
        ),
        migrations.RenameField(
            model_name='nhanvien',
            old_name='ename',
            new_name='nvname',
        ),
    ]
