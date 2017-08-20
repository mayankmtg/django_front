# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assessment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='link',
            field=models.CharField(default=b'', unique=True, max_length=250, blank=True),
        ),
    ]
