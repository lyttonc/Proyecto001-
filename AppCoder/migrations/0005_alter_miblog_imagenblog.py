# Generated by Django 4.1.7 on 2023-04-19 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_miblog_imagenblog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miblog',
            name='imagenblog',
            field=models.ImageField(null=True, upload_to='image_blog'),
        ),
    ]
