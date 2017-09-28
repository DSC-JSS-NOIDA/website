# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-28 04:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField()),
                ('speaker', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('reg_link', models.URLField(max_length=120)),
                ('created_by', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('img', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='events/', width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='events/', width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('slug', models.SlugField(blank=True, max_length=40, null=True)),
                ('github_repo', models.CharField(blank=True, max_length=100, null=True)),
                ('live_link', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='projects/')),
                ('main_image', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=True)),
                ('pic', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='team/', width_field='width_field')),
                ('height_field', models.IntegerField(blank=True, default=0)),
                ('width_field', models.IntegerField(blank=True, default=0)),
                ('year', models.IntegerField(blank=True, default=0)),
                ('github_link', models.URLField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=250, null=True)),
                ('linkedin', models.URLField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('user_id', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='contributors',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Team'),
        ),
        migrations.AddField(
            model_name='contributors',
            name='project',
            field=models.ManyToManyField(to='mainapp.Project'),
        ),
    ]
