# Generated by Django 3.2.16 on 2023-04-12 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20230331_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='color',
            field=models.CharField(default='#000000', max_length=7),
        ),
    ]
