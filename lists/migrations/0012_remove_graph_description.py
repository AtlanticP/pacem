# Generated by Django 2.0.4 on 2018-08-08 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0011_graph'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graph',
            name='description',
        ),
    ]
