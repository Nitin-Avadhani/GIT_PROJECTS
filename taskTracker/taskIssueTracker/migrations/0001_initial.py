# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IssueList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usernameid', models.CharField(max_length=200)),
                ('projectid', models.CharField(max_length=200)),
                ('issue', models.CharField(max_length=1000)),
                ('owner', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=100)),
                ('comments', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'db_issuelist',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usernameid', models.CharField(max_length=200)),
                ('projectname', models.CharField(max_length=200)),
                ('projectid', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'db_project',
            },
        ),
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usernameid', models.CharField(max_length=200)),
                ('projectid', models.CharField(max_length=200)),
                ('task', models.CharField(max_length=1000)),
                ('owner', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=100)),
                ('comments', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'db_tasklist',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('usernameid', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'db_user',
            },
        ),
    ]
