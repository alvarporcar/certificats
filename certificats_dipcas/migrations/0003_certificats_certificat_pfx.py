# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('certificats_dipcas', '0002_auto_20151203_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificats',
            name='certificat_pfx',
            field=models.FileField(default=datetime.datetime(2015, 12, 3, 22, 34, 11, 496459, tzinfo=utc), upload_to=b'.'),
            preserve_default=False,
        ),
    ]
