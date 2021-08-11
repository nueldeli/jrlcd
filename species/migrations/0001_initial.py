# Generated by Django 3.2.6 on 2021-08-11 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_input', models.DateTimeField(auto_now_add=True)),
                ('local_name', models.CharField(max_length=100)),
                ('scientific_name', models.CharField(max_length=100)),
                ('origin', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('species_img', models.ImageField(upload_to='')),
            ],
            options={
                'ordering': ['-date_input'],
            },
        ),
    ]
