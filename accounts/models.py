# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,AbstractUser, AbstractBaseUser,PermissionsMixin,Group,_user_has_perm
)

from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
import json
from django.db.models import Q


# python manage.py dumpdata dma --format json --indent 4 > dma/dmadd.json
# python manage.py loaddata dma/dmadd.json 


class UserProfile(AbstractUser):
    head_img = models.ImageField(upload_to='user/%Y/%m', verbose_name='头像', blank=True, default='', max_length=500)
    mobile = models.CharField(verbose_name='联系方式', max_length=11)
    wechat = models.CharField(verbose_name='微信', max_length=100)
    integral = models.IntegerField(default=0, verbose_name='积分')
    balance = models.DecimalField(decimal_places=2, max_digits=8,default=0.0, verbose_name='余额')
    open_id = models.CharField(max_length=100, verbose_name='OpenId')
    remark = models.TextField(verbose_name='备注')

    uuid        = models.CharField(max_length=300,null=True,blank=True)

    def __str__(self):
        return self.username

    class Meta:
        managed = True
        db_table = 'userprofile'
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name


class UserAddress(models.Model):
    user = models.ForeignKey(UserProfile, null=True, blank=True, verbose_name='用户',on_delete=models.CASCADE)
    address = models.CharField(max_length=500, verbose_name='收件地址')
    name = models.CharField(max_length=20, verbose_name='收件人')
    mobile = models.CharField(max_length=30, verbose_name='手机号')

    def __str__(self):
        return self.address

    class Meta:
        managed = True
        db_table = 'useraddress'
        verbose_name = '用户地址'
        verbose_name_plural = verbose_name


from jujulong.utils import unique_uuid_generator,unique_cid_generator

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.uuid:
        # instance.slug = create_slug(instance)
        instance.uuid = unique_uuid_generator(instance)
        instance.set_password(instance.password)

    


pre_save.connect(pre_save_post_receiver, sender=UserProfile)

       