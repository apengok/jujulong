# Generated by Django 2.0 on 2019-05-09 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20190509_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='品牌介绍'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='place',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='产地'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='website',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='官网'),
        ),
        migrations.AlterField(
            model_name='color',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='barcode',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='条码'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='cost_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='成本价'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='details',
            field=models.TextField(blank=True, null=True, verbose_name='详情'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product/%Y/%m', verbose_name='产品图片'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='keywords',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='关键词'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='market_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='市场价'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='产品名称'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='售价'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='unit',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='单位'),
        ),
        migrations.AlterField(
            model_name='size',
            name='cup',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='罩杯'),
        ),
        migrations.AlterField(
            model_name='size',
            name='others',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='其他'),
        ),
    ]
