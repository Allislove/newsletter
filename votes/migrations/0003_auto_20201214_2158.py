# Generated by Django 2.2.14 on 2020-12-15 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0002_auto_20201214_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='date',
            field=models.DateField(),
        ),
    ]
