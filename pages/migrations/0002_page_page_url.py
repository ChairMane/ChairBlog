# Generated by Django 3.0.4 on 2020-04-24 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='page_url',
            field=models.CharField(default='', max_length=40),
        ),
    ]