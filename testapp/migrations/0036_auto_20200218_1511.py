# Generated by Django 2.2.10 on 2020-02-18 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0035_auto_20200216_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='col_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='收藏时间'),
        ),
        migrations.AlterField(
            model_name='c_collection',
            name='is_look',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=10, verbose_name='已查看'),
        ),
        migrations.AlterField(
            model_name='information',
            name='is_hot',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=10, verbose_name='首页轮播'),
        ),
    ]
