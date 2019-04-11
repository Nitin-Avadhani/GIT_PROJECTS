# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskIssueTracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='taskid',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
