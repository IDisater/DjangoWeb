# Generated by Django 2.2.6 on 2019-12-04 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20191204_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='information',
            name='job',
            field=models.CharField(default='', max_length=20, verbose_name='职位'),
        ),
    ]
