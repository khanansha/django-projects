# Generated by Django 2.2.4 on 2019-12-13 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0007_auto_20191213_1220'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blogpost',
        ),
        migrations.AlterField(
            model_name='about',
            name='chead',
            field=models.CharField(default='', max_length=5000000),
        ),
        migrations.AlterField(
            model_name='about',
            name='head',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
