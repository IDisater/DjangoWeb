# Generated by Django 2.2.10 on 2020-02-13 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0031_auto_20200213_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='pay',
            field=models.CharField(default='3000-50001', max_length=50, verbose_name='薪酬'),
        ),
        migrations.AlterField(
            model_name='c_collection',
            name='is_look',
            field=models.CharField(choices=[('no', 'no'), ('yes', 'yes')], default='no', max_length=10, verbose_name='已查看'),
        ),
        migrations.AlterField(
            model_name='information',
            name='is_hot',
            field=models.CharField(choices=[('no', 'no'), ('yes', 'yes')], default='no', max_length=10, verbose_name='首页轮播'),
        ),
    ]
