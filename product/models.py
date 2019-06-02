# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.

from datetime import datetime

from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Category(MPTTModel):
    name = models.CharField(max_length=500, verbose_name='分类名称')
    sort = models.IntegerField(default=0, verbose_name='排序值')
    # parent = models.ForeignKey('self', default=0, null=True, blank=True, related_name='children', verbose_name='上级分类',
    #                            limit_choices_to={'is_abort': False, 'is_root': True})
    is_root = models.BooleanField(default=False, verbose_name='是否是一级分类')
    image = models.ImageField(upload_to='category/%Y/%m', verbose_name='分类图片', null=True, blank=True)
    is_abort = models.BooleanField(default=False, verbose_name='是否删除')

    parent  = TreeForeignKey('self', null=True, blank=True,on_delete=models.CASCADE, related_name='children', db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']


    class Meta:
        managed = True
        db_table = 'category'
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Brand(models.Model):
    # category    = models.ForeignKey(Category, verbose_name='分类', null=True, blank=True,on_delete=models.CASCADE)
    name        = models.CharField(max_length=500, verbose_name='品牌名称')
    place       = models.CharField(max_length=500, verbose_name='产地', null=True, blank=True)
    website     = models.CharField(max_length=500, verbose_name='官网', null=True, blank=True)
    description = models.TextField(verbose_name='品牌介绍', null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'brand'
        verbose_name = '品牌'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=100, verbose_name='颜色')
    description = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'productcolor'
        verbose_name = '颜色'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Size(models.Model):
    size    = models.CharField(max_length=100, verbose_name='型号')
    cup     = models.CharField(max_length=100, verbose_name='罩杯', null=True, blank=True)
    others  = models.CharField(max_length=100, verbose_name='其他', null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'productsize'
        verbose_name = '型号'
        verbose_name_plural = verbose_name

    def __str__(self):
        cup = self.cup
        if self.cup is None:
            cup = ''
        return "{}{}".format(self.size,cup)

class Goods(models.Model):
    STATUS_CHOICES = (
        (0, '下架'),
        (1, '上架'),
    )

    category    = models.ForeignKey(Category, verbose_name='分类', null=True, blank=True,on_delete=models.CASCADE,
                                 limit_choices_to={'is_abort': False})
    brand       = models.ForeignKey(Brand,verbose_name='品牌',null=True,blank=True,on_delete=models.SET_NULL)
    color       = models.ForeignKey(Color,verbose_name='颜色',null=True,blank=True,on_delete=models.SET_NULL)
    size        = models.ForeignKey(Size,verbose_name='型号',null=True,blank=True,on_delete=models.SET_NULL)
    name        = models.CharField(max_length=500, verbose_name='产品名称', null=True, blank=True)
    unit        = models.CharField(max_length=100, verbose_name='单位', null=True, blank=True)
    keywords    = models.CharField(max_length=200, verbose_name='关键词', null=True, blank=True)
    image       = models.ImageField(upload_to='product/%Y/%m', verbose_name='产品图片', null=True, blank=True)
    barcode     = models.CharField(max_length=100, verbose_name='条码', null=True, blank=True)
    price       = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='售价', null=True, blank=True)
    market_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='市场价', null=True, blank=True)
    cost_price  = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='成本价', null=True, blank=True)
    count       = models.IntegerField(default=0, verbose_name='库存')
    sales_count = models.IntegerField(default=0, verbose_name='售出数量')
    is_show_sales_count = models.BooleanField(default=False, verbose_name='显示销量')
    has_invoice = models.BooleanField(default=False, verbose_name='提供发票')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    status      = models.IntegerField(choices=STATUS_CHOICES, verbose_name='状态')
    no_search   = models.BooleanField(default=False, verbose_name='搜索是否显示')
    cannot_refund = models.BooleanField(default=False, verbose_name='支持退换货')
    order_value = models.IntegerField(default=0, verbose_name='排序值')
    view_count  = models.IntegerField(default=0, verbose_name='浏览量')
    details     = models.TextField(verbose_name='详情', null=True, blank=True)
    is_abort    = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta: 
        managed = True
        db_table = 'goods'
        verbose_name = '产品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}{}{}{}".format(self.brand.name,self.category.name,self.color.name,self.size.size)
