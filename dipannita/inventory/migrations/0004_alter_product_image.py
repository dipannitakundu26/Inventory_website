# Generated by Django 3.2.6 on 2021-12-31 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20211231_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='inventory/images'),
        ),
    ]
