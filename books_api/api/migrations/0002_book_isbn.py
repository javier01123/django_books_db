# Generated by Django 4.0.3 on 2022-03-20 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(default=None, max_length=13, null=True, unique=True),
        ),
    ]
