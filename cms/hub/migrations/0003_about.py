# Generated by Django 2.2.4 on 2019-12-11 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('head', models.CharField(max_length=100)),
                ('chead', models.CharField(max_length=5000000)),
            ],
        ),
    ]
