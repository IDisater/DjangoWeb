# Generated by Django 2.2.6 on 2019-12-07 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0021_c_collection_info_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='user_name',
            field=models.CharField(default='', max_length=128),
        ),
    ]
