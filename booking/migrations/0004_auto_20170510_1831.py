# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-10 18:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0003_remove_show_theatre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Waves Cinema', max_length=50)),
                ('city', models.CharField(choices=[('DELHI', 'Delhi'), ('KOLKATA', 'Kolkata'), ('MUMBAI', 'Mumbai'), ('CHENNAI', 'Chennai'), ('BANGALORE', 'Bangalore'), ('HYDERABAD', 'Hyderabad')], max_length=9)),
                ('address', models.CharField(max_length=30)),
                ('no_of_screen', models.IntegerField()),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='show',
            name='screen',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='show',
            name='theatre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.Theatre'),
        ),
    ]