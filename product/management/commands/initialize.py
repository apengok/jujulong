from django.core.management.base import BaseCommand, CommandError
from django.db import connections

from product.models import (Category,Goods,Color,Size,Brand)

import time
import datetime
import logging
import threading
# import Queue

import MySQLdb

from functools import wraps
from django.db import connection
from django.db.utils import IntegrityError

def db_auto_reconnect(func):
    """Auto reconnect db when mysql has gone away."""
    @wraps(func)
    def wrapper(*args, **kwagrs):
        try:
            connection.connection.ping()
        except Exception:
            connection.close()
        return func(*args, **kwagrs)
    return wrapper

logger_info = logging.getLogger('info_logger')


def close_old_connections():
    for conn in connections.all():
        conn.close_if_unusable_or_obsolete()




class Command(BaseCommand):
    help = 'import data from A to B'

    def add_arguments(self, parser):
        # parser.add_argument('sTime', type=str)

        parser.add_argument(
            '--color',
            action='store_true',
            dest='color',
            default=False,
            help='check color data'
        )        

        parser.add_argument(
            '--size',
            action='store_true',
            dest='size',
            default=False,
            help='check size data'
        )        

        parser.add_argument(
            '--brand',
            action='store_true',
            dest='brand',
            default=False,
            help='brand repeted data'
        )    

        parser.add_argument(
            '--category',
            action='store_true',
            dest='category',
            default=False,
            help='category repeted data'
        )        

        parser.add_argument(
            '-d',
            '--day',
            type=str,
            
            help='query by day'
        )

        parser.add_argument(
            '--hour',
            type=str,
            
            help='query by hour'
        )

        parser.add_argument(
            '-m',
            '--month',
            type=str,
            
            help='query by month'
        )

        parser.add_argument(
            '--syncbigmeter',
            action='store_true',
            dest='syncbigmeter',
            default=False,
            help='syncbigmeter  data'
        )  

    def handle(self, *args, **options):
        
        t1=time.time()
        count = 0
        if options['category']:
            init_category(**options)
        if options['brand']:
            init_brand(**options)
        if options['color']:
            init_color(**options)
        if options['size']:
            init_size(**options)

        print('Finished')


def init_category(**options):
    
    categories = ['内衣','内裤','袜子','塑身衣','其他']

    

    all_categories = [{'name':c,'sort':n} for n,c in enumerate(categories,start=1)]

    added_list = []
    for c in all_categories:
        Category.objects.create(**c)

    if len(added_list) > 0:
        Category.objects.bulk_create(added_list)

    
        

def init_brand(**options):
    BRA,UNDERWEAR,SOCKS,SLIMMING,OTHER = range(1,6)
    brand = [(BRA,'金薇'),(BRA,'林夕梦'),(BRA,'歌瑞森'),(SLIMMING,'幸福狐狸'),(UNDERWEAR,'维也纳的秘密'),(SOCKS,'0.18'),(OTHER,'正姿护眼笔')]

    added_list = []
    for k,v in brand:
        Brand.objects.create(name=v)

# 初始化产品颜色
def init_color(**options):
    all_colors = [
        {'name':'黑色','description':'black'},
        {'name':'白色','description':'white'},
        {'name':'红色','description':'red'},
        {'name':'粉色','description':'pink'},
        {'name':'蓝色','description':'blue'},
        {'name':'绿色','description':'green'},
        {'name':'灰色','description':'grey'},
    ]

    added_list = []

    for c in all_colors:
        added_list.append(Color(**c))

    if len(added_list)>0:
        Color.objects.bulk_create(added_list)



             
# 初始化产品size
def init_size(**options):
    size = ['70','75','80','85','90','95']
    cups  = ['A','B','C','D','E']
    others = []
    all_bra_sizes = [{'size':s,'cup':c} for s in size for c in cups]
    # print(all_bra_sizes)
    

    added_list = []

    for c in all_bra_sizes:
        added_list.append(Size(**c))

    if len(added_list)>0:
        Size.objects.bulk_create(added_list)

             
