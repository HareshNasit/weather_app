# Generated by Django 2.2.1 on 2019-05-19 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='feature',
            field=models.BooleanField(null=True),
        ),
    ]