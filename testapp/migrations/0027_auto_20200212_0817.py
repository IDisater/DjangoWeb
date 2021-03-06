# Generated by Django 2.2.6 on 2020-02-12 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0026_auto_20200211_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='c_collection',
            name='c_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='投递时间'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='com_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='company',
            name='createdate',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='information',
            name='createdate',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='createdate',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
    ]
