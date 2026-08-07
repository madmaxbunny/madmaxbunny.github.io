---
title: "JEUS8"
date: "2020-04-17T14:47:57+09:00"
category: "프로그래밍/System"
tags: []
original_url: "https://priv.tistory.com/88"
tistory_id: 88
---

[build-real-server-all.sh](build-real-server-all.sh)

#!/bin/bash   
  
./[build-real-server-01.sh](build-real-server-01.sh)   
./[build-real-server-02.sh](build-real-server-02.sh)  
---  
  
[build-real-server-01.sh](build-real-server-01.sh)

#!/bin/bash   
  
ant   
  
  
ssh msfa@ip주소 '/home/msfa/mtsfa-workspace/[stop-server.sh'](stop-server.sh')   
  
ssh msfa@ip주소 '/home/msfa/mtsfa-workspace/[delete-cash.sh'](delete-cash.sh')   
  
scp ./deploy/[mtsfa.war](mtsfa.war) msfa@ip주소:/tmax/lemp/war/   
scp -r ./deploy/conf/sql/MTSFA/* msfa@ip주소:/tmax/lemp/conf/sql/MTSFA/   
  
ssh msfa@ip주소 '/home/msfa/mtsfa-workspace/[start-server.sh'](start-server.sh')   
rm -r ./deploy/  
---  
  
[build-real-server-02.sh](build-real-server-02.sh)

#!/bin/bash   
  
ant   
  
ssh msfa@ip주소 '/home/msfa/mtsfa-workspace/[stop-server.sh'](stop-server.sh')   
  
ssh msfa@ip주소 '/home/msfa/mtsfa-workspace/[delete-cash.sh'](delete-cash.sh')   
  
scp ./deploy/[mtsfa.war](mtsfa.war) msfa@ip주소:/tmax/lemp/war/   
scp -r ./deploy/conf/sql/MTSFA/* msfa@ip주소:/tmax/lemp/conf/sql/MTSFA/   
  
ssh msfa@ip주소 '/home/msfa/mtsfa-workspace/[start-server.sh'](start-server.sh')   
rm -r ./deploy/   
---  
  
[stop-server.sh](stop-server.sh')

#!/bin/bash   
  
  
/tmax/jeus8/bin/jeusadmin -host LCSSFAAP01:10000 -u administrator -p password "stopserver sfa2_mt01 -to 120"   
---  
  
[delete-cash.sh](delete-cash.sh')

#!/bin/bash   
  
rm -r /tmax/jeus8/domains/msfa_domain/.downloaded/.applications/sta2_mt02   
rm -r /tmax/jeus8/domains/msfa_domain/servers/sfa2_mt02   
rm /tmax/lemp/war/[mtsfa.war](mtsfa.war)  
---  
  
[start-server.sh](start-server.sh)

#!/bin/bash   
  
  
/tmax/jeus8/bin/jeusadmin -host LCSSFAAP01:10000 -u administrator -p password "startserver sfa2_mt01"   
---
