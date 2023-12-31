# Generated by Django 3.2.19 on 2023-07-06 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DigitalArtWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('daw_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField()),
                ('size', models.CharField(blank=True, max_length=254, null=True)),
                ('file_type', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
