# Generated by Django 2.2.14 on 2020-12-15 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]