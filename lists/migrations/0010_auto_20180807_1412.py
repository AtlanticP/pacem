# Generated by Django 2.0.4 on 2018-08-07 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0009_auto_20180807_1320'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Graph',
        ),
        migrations.AlterField(
            model_name='item',
            name='lst',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='lists.List'),
        ),
    ]
