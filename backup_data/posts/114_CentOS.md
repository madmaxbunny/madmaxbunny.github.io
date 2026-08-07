---
title: "CentOS"
date: "2022-10-26T02:31:47+09:00"
category: "카테고리 없음"
tags: []
original_url: "https://priv.tistory.com/114"
tistory_id: 114
---

1\. 방화벽
    
    
    ```bash
    yum install net-tools			# netstat 설치
    
    netstat -tnlp				# 열린 포트 확인
    
    firewall-cmd --permanent --zone=public --add-port=8080/tcp		# 포트 오픈
    firewall-cmd --reload			# 재시작
    ```
    
