# Generated by Django 3.2.19 on 2023-07-08 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20230708_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='variation',
        ),
    ]
