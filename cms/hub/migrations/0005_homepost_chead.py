# Generated by Django 2.2.4 on 2019-12-11 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0004_auto_20191211_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepost',
            name='chead',
            field=models.CharField(default='', max_length=50000),
        ),
    ]
