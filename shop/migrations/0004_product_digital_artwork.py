# Generated by Django 3.2.19 on 2023-07-08 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digital_artworks', '0002_auto_20230706_1420'),
        ('shop', '0003_remove_subcategory_variation'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='digital_artwork',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='digital_artworks.digitalartwork'),
        ),
    ]