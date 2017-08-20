# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('link', models.CharField(default=b'', max_length=250, blank=True)),
                ('name', models.CharField(max_length=250)),
                ('desc', models.CharField(max_length=250)),
                ('duration', models.IntegerField(default=30)),
                ('positive', models.IntegerField(default=4)),
                ('negative', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=1250)),
                ('A', models.CharField(max_length=250)),
                ('B', models.CharField(max_length=250)),
                ('C', models.CharField(max_length=250)),
                ('D', models.CharField(max_length=250)),
                ('ans', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='questionBank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill', models.CharField(max_length=250)),
                ('questionBank', models.ForeignKey(to='Assessment.questionBank')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='questionBank',
            field=models.ForeignKey(to='Assessment.questionBank'),
        ),
        migrations.AddField(
            model_name='question',
            name='skill1',
            field=models.ForeignKey(related_name='skill1', to='Assessment.Skill'),
        ),
        migrations.AddField(
            model_name='question',
            name='skill2',
            field=models.ForeignKey(related_name='skill2', to='Assessment.Skill'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='bank',
            field=models.ForeignKey(to='Assessment.questionBank'),
        ),
    ]
