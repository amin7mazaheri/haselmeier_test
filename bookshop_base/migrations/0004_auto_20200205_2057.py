# Generated by Django 2.2 on 2020-02-05 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop_base', '0003_auto_20200205_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
