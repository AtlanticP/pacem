# Generated by Django 2.0.4 on 2018-04-27 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_auto_20180427_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='list',
            name='lan',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
    ]