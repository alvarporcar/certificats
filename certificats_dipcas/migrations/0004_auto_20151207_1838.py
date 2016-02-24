# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificats_dipcas', '0003_certificats_certificat_pfx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificats',
            name='certificat_pfx',
        ),
        migrations.AddField(
            model_name='certificats',
            name='data_fi',
            field=models.DateField(default=b'2015-01-01'),
        ),
        migrations.AddField(
            model_name='certificats',
            name='data_inici',
            field=models.DateField(default=b'2015-01-01'),
        ),
        migrations.AddField(
            model_name='certificats',
            name='segell',
            field=models.BooleanField(default=b'True'),
        ),
    ]
