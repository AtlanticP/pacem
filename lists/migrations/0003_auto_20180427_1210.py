# Generated by Django 2.0.4 on 2018-04-27 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20180427_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(),
        ),
    ]
