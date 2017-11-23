#!/usr/bin/env python
#coding=utf8
from tornado import gen
from tornado.ioloop import IOLoop

from tornadohttpclient import TornadoHTTPClient
import json
# 实例化
http = TornadoHTTPClient()

@gen.coroutine
def get():
    headers = dict((("content-type","application/json"),("Accept-Charset","utf8"),("Authorization","token F017254EAF208C462C8D4ABCBC27F1DD7CB8DA65FF70B063CF16E90AA35BAE7FAF360C87D0617ED7723DC64FC8CA6A47438F5BED9FC60C303DF3AFAAE2C44A8FAE961E8999B43C820615D9489DA0AB178368A3F9CA7640CA755283A67E8D9CC13DA55AFD48606621E37C601A52E64C94530C92D468CF5A72DE68C0F7230103F400A855997086CE4E4E357BB887D0B08C6D5238EA6B5487E0231A10B38650FEE92D14264704D3FC1C80AC6675612E41C17A73D9283470A0C1FBB8C089106169AB6C179C296D073F09FDB1822646AE5B76D458CC433C1F4829AC2DACE160F851188951ED2BF00CA6E4AA53CFCC659C100F53669EB2C9F4DDAA5BBB1C5D8E98EFB720C94AA3") ))
    # 发出get请求
    # response = yield #http.post("http://ipsapro.isoftstone.com:8081/api/user/login",'{"strUser":"admin","strPwd":"e10adc3949ba59abbe56e057f20f883ee10adc3949ba59abbe56e057f20f883e"}',headers=headers)

    response = yield http.post("http://ipsapro.isoftstone.com:8081/api/Department/GetDepartment",'',headers=headers);
    # print(response.body)
    fo = open("department.txt", "wb")
    #j=json.loads(response.body)
    #str_json=json.dumps(j['departments'],encoding="gbk",ensure_ascii=False)
    str_json=response.body
    fo.write(str_json)
IOLoop.instance().run_sync(get)
