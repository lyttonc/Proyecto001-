# Generated by Django 4.1.7 on 2023-04-18 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='miblog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('subtitulo', models.CharField(max_length=100)),
                ('cuerpo', models.CharField(max_length=100000)),
                ('imagenblog', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
    ]
