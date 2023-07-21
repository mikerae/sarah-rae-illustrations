# Generated by Django 3.2.20 on 2023-07-21 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('checkout', '0005_alter_order_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_prifile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='profiles.userprofile'),
        ),
    ]