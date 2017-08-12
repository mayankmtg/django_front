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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.CharField(max_length=250)),
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
                ('skill1', models.CharField(max_length=250)),
                ('skill2', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='questionBank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('question1', models.ForeignKey(related_name='question1', to='Assessment.Question')),
                ('question10', models.ForeignKey(related_name='question10', to='Assessment.Question')),
                ('question2', models.ForeignKey(related_name='question2', to='Assessment.Question')),
                ('question3', models.ForeignKey(related_name='question3', to='Assessment.Question')),
                ('question4', models.ForeignKey(related_name='question4', to='Assessment.Question')),
                ('question5', models.ForeignKey(related_name='question5', to='Assessment.Question')),
                ('question6', models.ForeignKey(related_name='question6', to='Assessment.Question')),
                ('question7', models.ForeignKey(related_name='question7', to='Assessment.Question')),
                ('question8', models.ForeignKey(related_name='question8', to='Assessment.Question')),
                ('question9', models.ForeignKey(related_name='question9', to='Assessment.Question')),
            ],
        ),
        migrations.AddField(
            model_name='assessment',
            name='bank',
            field=models.ForeignKey(to='Assessment.questionBank'),
        ),
    ]
