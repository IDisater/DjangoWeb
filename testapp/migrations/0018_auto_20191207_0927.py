# Generated by Django 2.2.6 on 2019-12-07 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0017_auto_20191207_0856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='c_collection',
            name='cp_title',
        ),
        migrations.AddField(
            model_name='c_collection',
            name='cp_name',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='c_collection',
            name='user_name',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='comments',
            name='user_title',
            field=models.CharField(default='', max_length=30, verbose_name='昵称'),
        ),
    ]
