# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myLesson', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name=b'\xb1\xea\xcc\xe2')),
                ('content', models.TextField(verbose_name=b'\xc4\xda\xc8\xdd')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xb7\xa2\xb1\xed\xca\xb1\xbc\xe4')),
                ('update_time', models.DateField(auto_now=True, verbose_name=b'\xb8\xfc\xd0\xc2\xca\xb1\xbc\xe4', null=True)),
            ],
        ),
    ]
