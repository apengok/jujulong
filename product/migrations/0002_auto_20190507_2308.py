# Generated by Django 2.0 on 2019-05-07 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='颜色')),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'productcolor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=100, verbose_name='型号')),
                ('cup', models.CharField(max_length=100, verbose_name='罩杯')),
                ('others', models.CharField(max_length=100, verbose_name='罩杯')),
            ],
            options={
                'db_table': 'productsize',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Color', verbose_name='颜色'),
        ),
        migrations.AddField(
            model_name='goods',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Size', verbose_name='型号'),
        ),
    ]
