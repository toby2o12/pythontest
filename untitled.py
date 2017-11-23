# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#!/usr/bin/python3
# encoding=utf8
import sys

import pymysql


# print(sys.getdefaultencoding())

# Connect to the database
connection = pymysql.connect(host='10.129.130.44',
                             user='admin',
                             password='admin123',
                             db='srsdb',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "select * from srs_user srs_user"
        cursor.execute(sql, ())

         # 获取查询结果

        result = cursor.fetchone()

        print(result['display_name'])

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    # connection.commit()
finally:

    connection.close()
