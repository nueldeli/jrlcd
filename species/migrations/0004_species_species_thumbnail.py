# Generated by Django 3.2.6 on 2021-09-20 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('species', '0003_auto_20210819_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='species_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='species_thumbnail', verbose_name='Species thumbnail'),
        ),
    ]
