# Generated by Django 2.0.5 on 2020-08-01 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190326_1754'),
        ('dashboard_live', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='dashboard',
            new_name='dashboard_live',
        ),
        migrations.RenameModel(
            old_name='stripeUser',
            new_name='stripeUser_live',
        ),
    ]
