# Generated by Django 2.0 on 2019-05-09 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20190508_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='others',
            field=models.CharField(max_length=100, verbose_name='其他'),
        ),
    ]
