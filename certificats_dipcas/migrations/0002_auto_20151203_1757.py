# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificats_dipcas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificats',
            name='certificat',
            field=models.FileField(upload_to=b'.'),
        ),
        migrations.AlterField(
            model_name='certificats',
            name='clau',
            field=models.FileField(upload_to=b'.'),
        ),
    ]
