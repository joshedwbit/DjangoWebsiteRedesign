# Generated by Django 4.2 on 2023-08-06 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideapadapp1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='AboutMe',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='Aim',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='Approach',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='Background',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='Title',
            field=models.CharField(max_length=50),
        ),
    ]
