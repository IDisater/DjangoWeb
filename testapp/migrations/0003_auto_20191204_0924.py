# Generated by Django 2.2.6 on 2019-12-04 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20191128_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='C_collection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.CharField(max_length=256)),
                ('cp_id', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'C_col',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.CharField(max_length=256)),
                ('info_id', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'Col',
            },
        ),
        migrations.AlterField(
            model_name='company',
            name='cp_name',
            field=models.CharField(max_length=128, verbose_name='账号'),
        ),
        migrations.AlterField(
            model_name='company',
            name='password',
            field=models.CharField(max_length=256, verbose_name='密码'),
        ),
        migrations.AddField(
            model_name='relationship',
            name='col',
            field=models.ManyToManyField(to='testapp.Collection'),
        ),
    ]
