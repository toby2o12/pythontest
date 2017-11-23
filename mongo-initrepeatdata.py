# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pymongo

client=pymongo.MongoClient('10.129.132.114',27017)
# client=pymongo.MongoClient('10.10.11.58',27017)
db=client.resumedb

# 分页获取数据,name,email,phone
total=db.resume_new.count()
print('total is '+str(total))
skip=453600
limit=200
t_tmp=total
fo = open("resume.txt", "a+")
idx=0;
while (t_tmp>0):
    array=db.resume_new.find({},{'contact.phone':1,'basic.name':1,'contact.email':1,'increment_id':1}).sort('increment_id', pymongo.ASCENDING).limit(limit).skip(skip)
    row=0
    for k, v in enumerate(array):
        idx=idx+1
        row=row+1

        str_r='{'+str(idx)+'},{'+str(v['increment_id'])+'},'+'{'+str(v['basic']['name'])+'},{'+str(v['contact']['email'])+'},{'+str(v['contact']['phone'])+'}\n'
        # print(str_r)
        fo.write(str_r)
    skip+=row
    if row==0:
        break
    if(skip%5000==0):
        print('current skip '+ str(skip))
    #if(skip>=20):
    #    break
fo.close()
