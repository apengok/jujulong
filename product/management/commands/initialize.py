from django.core.management.base import BaseCommand, CommandError
from django.db import connections

from product.models import (Category,Goods,Color,Size)

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
            '--delete',
            action='store_true',
            dest='delete',
            default=False,
            help='delete repeted data'
        )    

        parser.add_argument(
            '--realtime',
            action='store_true',
            dest='realtime',
            default=False,
            help='realtime repeted data'
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
        if options['color']:
            init_color(**options)

        

# 按月同步数据
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

             
