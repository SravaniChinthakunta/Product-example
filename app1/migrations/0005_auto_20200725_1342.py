# Generated by Django 3.0.7 on 2020-07-25 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20200725_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='file',
            field=models.FileField(default=False, upload_to='myfiles/'),
        ),
    ]