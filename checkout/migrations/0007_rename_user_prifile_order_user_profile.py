# Generated by Django 3.2.20 on 2023-07-22 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_order_user_prifile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user_prifile',
            new_name='user_profile',
        ),
    ]