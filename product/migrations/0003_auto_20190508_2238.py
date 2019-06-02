# Generated by Django 2.0 on 2019-05-08 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20190507_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='品牌名称')),
                ('place', models.CharField(max_length=500, verbose_name='产地')),
                ('website', models.CharField(max_length=500, verbose_name='官网')),
                ('description', models.CharField(max_length=500, verbose_name='品牌介绍')),
            ],
            options={
                'verbose_name': '品牌',
                'verbose_name_plural': '品牌',
                'db_table': 'brand',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'managed': True, 'verbose_name': '颜色', 'verbose_name_plural': '颜色'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'managed': True, 'verbose_name': '型号', 'verbose_name_plural': '型号'},
        ),
        migrations.AddField(
            model_name='goods',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Brand', verbose_name='品牌'),
        ),
    ]