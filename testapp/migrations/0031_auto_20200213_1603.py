# Generated by Django 2.2.10 on 2020-02-13 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0030_auto_20200212_2225'),
    ]

    operations = [
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
