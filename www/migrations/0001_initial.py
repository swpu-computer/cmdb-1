# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-01 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='groupName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='salt_module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_module', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='webSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webSite', models.CharField(max_length=64)),
                ('lb_server', models.CharField(max_length=64)),
                ('salt_pillar_host', models.CharField(max_length=64)),
                ('svn_path', models.CharField(max_length=128)),
                ('svn_username', models.CharField(max_length=128)),
                ('svn_password', models.CharField(max_length=128)),
                ('svn_repo', models.CharField(max_length=128)),
                ('recycle_cmd', models.CharField(max_length=128)),
                ('env', models.IntegerField(choices=[(1, '\u751f\u4ea7\u73af\u5883'), (2, '\u6d4b\u8bd5\u73af\u5883')], verbose_name='\u8fd0\u884c\u73af\u5883')),
            ],
        ),
        migrations.CreateModel(
            name='webUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=64)),
                ('ip', models.GenericIPAddressField()),
            ],
        ),
        migrations.AddField(
            model_name='website',
            name='checkUrl',
            field=models.ManyToManyField(to='www.webUrl'),
        ),
        migrations.AddField(
            model_name='website',
            name='state_module',
            field=models.ManyToManyField(to='www.salt_module'),
        ),
        migrations.AddField(
            model_name='groupname',
            name='member',
            field=models.ManyToManyField(to='www.webSite'),
        ),
    ]
