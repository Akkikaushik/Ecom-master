# Generated by Django 2.2.14 on 2021-09-09 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aladin', '0010_auto_20210909_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ordered_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
    ]