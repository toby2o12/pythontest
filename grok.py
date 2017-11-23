

from pygrok import Grok
#text = 'gary is male, 25 years old and weighs 68.5 kilograms'
#text='INFO  2017-11-22 18:54:37,286 [116  ] loginfo                                  - -QResumeCurstate-Count:select count(1) from scp_trustresume_curstate where creator_id=1033 and changed_status in (101,302,402,602,702,902) and role=3'
#text = 'INFO  2017-11-22 18:48:26,832 [100  ] zzz                                - 2017-11-22 18:48,收到请求:url:http://localhost:9100/resumefmanage/lockreleaselist/list,path:/resumefmanage/lockreleaselist/list,data:,body:{"role":2,"menutype":35,"jobId":-1,"SearchName":null,"SkipCount":20,"MaxResultCount":10},user_id:1033'
#pattern = '%{WORD:name} is %{WORD:gender}, %{NUMBER:age} years old and weighs %{NUMBER:weight} kilograms'
#text ='ERROR  2017-10-23 02:52:41,923 [136  ] ECommon.Remoting.SocketRemotingClient - Reconnect to server error'
text = 'INFO  2017-11-23 14:04:55,134 [78   ] loginfo                                  - -QResumeCurstate-Count:select count(1) from scp_trustresume_curstate where creator_id=1033 and changed_status in (101,302,402,602,702,902) and role=3'
#pattern = '%{WORD:level}  %{TIMESTAMP_ISO8601:date} \[%{NUMBER}  \] %{DATA:LOGNAME}%{SPACE}-%{SPACE}%{GREEDYDATA}'
#pattern = '%{WORD:level}  %{TIMESTAMP_ISO8601:date} \[%{NUMBER}  \] (?<f>(request|zzz )) '
pattern = '%{WORD:level}%{SPACE}%{TIMESTAMP_ISO8601:date}%{SPACE}\[%{NUMBER}%{SPACE}\]%{SPACE}%{DATA:LOGNAME}%{SPACE}-%{SPACE}((%{GREEDYDATA},user_id:%{NUMBER:user_id})|%{GREEDYDATA})'
grok = Grok(pattern)
print(grok.match(text))

