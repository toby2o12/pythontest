# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pymongo


def show(uid):
	_oo=db.resume_new.find_one({'_id':uid})
	print(_oo['basic']['address'])
def updateAddress(uid,val):
	db.resume_new.update({'_id':uid},{'$set':{'basic.address':val}})

client=pymongo.MongoClient('10.129.132.114',27017)
# client=pymongo.MongoClient('10.10.11.58',27017)
db=client.resumedb

print(db.name)
skip=0;
while True:
	list =db.resume_new.find({}).sort("increment_id").skip(skip).limit(10)
	if list.count==0:
		break;
	skip=skip+list.count
	for k,v in enumerate(list):
		increment_id=v['increment_id']
		print(v['basic']['expect_bonus'])
		expect_bonus=v['basic']['expect_bonus'];
		if expect_bonus<0:
			print(expect_bonus)
print('complete')
'''
idarra=['7e342851-59c8-4072-83be-0ee732e8364d','3b68cd60-1ecd-4813-86f2-d98785dd8a0a'
,'d5f6ee50-abfc-4efd-a9c3-4c695d925f4d','9cd9e080-1c8b-4ede-ad10-0590f7baed1c'
,'7fced6a1-5d13-455a-b9eb-d9d0c0d62385','f1401b0d-3172-44e9-b170-fc32c4b62410'
,'ae51cef2-41e6-45aa-b935-9cb8be40036f','b78b85d6-dbff-45d0-977a-a05efb4d9da9'
,'2c1c8a1f-bf0c-4cda-aa80-7fdd75fb506d','8991d632-b9f2-4dee-bb0d-d98592a169d0']

for k, v in enumerate(idarra):
	one=db.resume_new.find_one({'_id':v},{'education':1,'work':1})
	print('work info')
	for q,w in enumerate(one['work']):
		print(w['start_time']+','+w['end_time'])
	print('education info')
	for q,w in enumerate(one['education']):
		print(w['start_time']+','+w['end_time'])
'''
'''
one=db.resume_new.find_one({'_id':'9f7addb3-095d-4c35-b423-ae21b1609a6c'})

print(one['basic']['address'])

db.resume_new.update({'_id':'9f7addb3-095d-4c35-b423-ae21b1609a6c'},{'$set':{'basic.address':321}})

one=db.resume_new.find_one({'_id':'9f7addb3-095d-4c35-b423-ae21b1609a6c'})

print(one['basic']['address'])

u105='1c3ed077-2d1a-4354-bd42-c4843987d20d'

show(u105)
db.resume_new.update({'_id':u105},{'$set':{'basic.address':105}})

show(u105)
print('update 231')
u231Arr=['a12ee676-0201-4b4c-989b-dc9c1bba8b66','ca6a13fa-2a0d-461e-a02f-746aa72ff617','c20ac952-20c4-40c1-9177-083fbf29b806']
for k, v in enumerate(u231Arr):
        show(v)
        updateAddress(v,231)
print('after update')
for k, v in enumerate(u231Arr):
        show(v)
print('update 33')
u33Arr=['59b0a11e-9693-482f-af5c-6ceac55befcf','5cd566f7-16b2-4216-90da-38ae78250bdf','faa9e8bd-781e-4a23-a24a-714b55287849','9b86f6ea-de36-4d90-b3c5-b7849dbcc552']

for k, v in enumerate(u33Arr):
        show(v)
        updateAddress(v,33)
print('after update')
for k, v in enumerate(u33Arr):
        show(v)
'''
