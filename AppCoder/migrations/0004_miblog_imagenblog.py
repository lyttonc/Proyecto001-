# Generated by Django 4.1.7 on 2023-04-19 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_remove_miblog_imagenblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='miblog',
            name='imagenblog',
            field=models.ImageField(blank=True, null=True, upload_to='avatar'),
        ),
    ]
