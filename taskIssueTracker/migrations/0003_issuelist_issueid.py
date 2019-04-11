# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskIssueTracker', '0002_tasklist_taskid'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuelist',
            name='issueid',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
