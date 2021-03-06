# Generated by Django 3.2.6 on 2021-08-19 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('species', '0002_alter_species_species_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='species',
            name='description',
        ),
        migrations.RemoveField(
            model_name='species',
            name='origin',
        ),
        migrations.RemoveField(
            model_name='species',
            name='scientific_name',
        ),
        migrations.AddField(
            model_name='species',
            name='species_type',
            field=models.CharField(choices=[('INDIGENOUS', 'Indigenous'), ('EXOTIC', 'Exotic')], default='INDIGENOUS', max_length=50),
        ),
    ]
