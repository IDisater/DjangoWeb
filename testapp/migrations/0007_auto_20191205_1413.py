# Generated by Django 2.2.6 on 2019-12-05 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_auto_20191204_1213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='userid',
            new_name='user_name',
        ),
    ]
