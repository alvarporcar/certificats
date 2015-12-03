# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('municipi', models.CharField(max_length=100)),
                ('certificat', models.FileField(upload_to=b'arxius/')),
                ('clau', models.FileField(upload_to=b'arxius/')),
            ],
        ),
    ]
