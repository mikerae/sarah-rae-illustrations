# Generated by Django 3.2.20 on 2023-07-20 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_cost',
        ),
        migrations.RemoveField(
            model_name='order',
            name='grand_total',
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]