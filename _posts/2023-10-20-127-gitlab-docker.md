---
title: Gitlab Docker
date: 2023-10-20 01:01:53 +0900
categories:
- 인프라
tags:
- gitlab
- nginx
---

Gitlab Docker에 대한 정리 노트이에요. 참고하시는 데 도움되었으면 해요.

---

## 개요 및 배경

Gitlab Docker에 관해 실무와 개발 과정에서 알게 된 핵심 내용들을 공유해요.

---

## 핵심 설명 및 코드

>  **TL;DR (핵심 요약)**  
> Gitlab Docker에 대한 상세 설명 및 핵심 가이드이에요.

---

## 개요 및 배경

Gitlab Docker 가이드 및 실무 적용 설명이에요.

---

## 핵심 설명 및 코드

### 1\. 설치

### 포트 점검
    
    
    ```bash
    > sudo netstat -ntlp | grep 80
    > sudo netstat -ntlp | grep 443
    ```
    

### 깃랩 이미지 pull
    
    
    ```bash
    > docker pull 넥서스주소/gitlab/gitlab-ce:latest
    ```
    

(host 파일 위치 : /etc/hosts)

### 환경 변수 추가 및 작업 디렉토리 생성
    
    
    ```bash
    > sudo vi /etc/profile
    export GITLAB_HOME=/srv/gitlab
    
    > mkdir /srv/gitlab/data
    > mkdir /srv/gitlab/logs
    > mkdir /srv/gitlab/config
    
    > sudo chmod -R 755 /srv/gitlab/data
    > sudo chmod -R 755 /srv/gitlab/logs
    > sudo chmod -R 755 /srv/gitlab/config
    ```
    

(환경 변수 추가 후 터미널 재가동 필요)

### 깃랩 실행
    
    
    ```bash
    > docker run --detach   --hostname gitlab.devlion.org   --publish 443:443 --publish 80:80 --publish 8022:22   --name gitlab   --restart always   --volume $GITLAB_HOME/config:/etc/gitlab   --volume $GITLAB_HOME/logs:/var/log/gitlab   --volume $GITLAB_HOME/data:/var/opt/gitlab   --volume $GITLAB_HOME/ssl:/etc/gitlab/ssl   --shm-size 1024m   넥서스주소/gitlab/gitlab-ce:latest
    ```
    

### 초기 패스워드 조회하는 법1 
    
    
    ```bash
    > cat /etc/gitlab/initial_root_password  | grep Password:
    Password: KWE8pVh+TuEH2QtaPCkGh3d0q081WL7zIrjNblQzXpY=
    ```
    

(ID는 root)

### 초기 패스워드 조회하는 법2
    
    
    ```bash
    > docker exec -it gitlab grep 'Password:' /etc/gitlab/initial_root_password
    Password: Hzr99gObApojTWemmhUADpACdbnorRhwfIKnTwjPv6Y=
    ```
    

* * *

## 2\. 이슈 

메일 발송   
<https://swealth.tistory.com/185>

SSL 설정 관련   
<https://www.psjco.com/56>  
<https://velog.io/@lazysoul/docker-gitlab>  
<https://blog.programster.org/dockerized-gitlab-configure-ssl>  
  
  
SSL certificate problem: unable to get local issuer certificate   
> git config --global http.sslVerify false   
<https://m.blog.naver.com/theswice/221715175304>

메일 발송   
<https://swealth.tistory.com/185>

메일 테스트
    
    
    ```bash
    > gitlab-rails console
    > Notify.test_email('khlim@hyundai-autoever.com', 'GitLab 메일링 테스트입니다', 'GitLab SMTP를 수정하였기에 메일링 테스트를 진행해요.').deliver_now
    ```
    

젠킨스에서 발생 시,   
SSL certificate problem: unable to get local issuer certificate   
git config --system http.sslVerify false

포트 확인   
nc -vz [IP] [PORT]   
nc -vz 10.0.0.1 8884

* * *

### 

### 1\. URL 설정
    
    
    ```bash
     external_url 'https://gitlab.devlion.org'
    ```
    

### 2\. 메일 설정
    
    
    ```bash
    gitlab_rails['smtp_enable'] = true
    gitlab_rails['smtp_address'] = "10.1.2.3"
    gitlab_rails['smtp_port'] = 25
    gitlab_rails['smtp_domain'] = "10.1.2.3"
    gitlab_rails['smtp_enable_starttls_auto'] = true
    gitlab_rails['smtp_tls'] = false
     
    gitlab_rails['smtp_openssl_verify_mode'] = 'none'
     
    gitlab_rails['gitlab_email_from'] = 'admin@devlion.org' // 송신자
    gitlab_rails['gitlab_email_display_name'] = 'Gitlab Manager'
    gitlab_rails['gitlab_email_reply_to'] = 'gitlab@naver.com' // 회신 시 메일 주소
    ```
    

### 3\. SSL 설정

### 

### 4\. Using a non-bundled web-server

\- Gitlab Docker 내 Nginx를 포함하지만, 별도 Nginx와 연계 방법

<https://docs.gitlab.com/omnibus/settings/nginx.html#using-a-non-bundled-web-server>

\- 가이드는 Nginx를 사용하지 않지만, 필자는 80을 열어두고 포워딩 받는 방법을 선택함
    
    
    ```bash
    gitlab_rails['trusted_proxies'] = ['10.1.2.3'] // 웹 서버(프록시) IP
    
    web_server['external_users'] = ['www-data']
    nginx['enable'] = true
    nginx['listen_port'] = 80
    nginx['listen_https'] = false
    ```
    

Nginx

* * *

## Gitlab 업데이트

보안 취약점 떄문에 운영 중인 Gitlab을 업데이트하며, 도움이 되었던 링크를 남겨 둠..

<https://run-think-dev.tistory.com/69>

<https://jiurinie.tistory.com/24>

<https://docs.gitlab.com/ee/update/?tab=Docker>

[https://gitlab-com.gitlab.io/support/toolbox/upgrade-path/?distro=docker&edition=ce&n1=true](https://gitlab-com.gitlab.io/support/toolbox/upgrade-path/?distro=docker&edition=ce&n1=true)

도커 백업

<https://www.lesstif.com/gitbook/gitlab-19857653.html>

---

## 정리하며

- 본 포스트는 실무 개발 및 인프라 운용 중 검증된 노하우를 바탕으로 정리되었습니다.
- 추가 문의나 개선사항은 포스트 하단 댓글 또는 GitHub 이슈로 전달해 주세요.

---

## 정리하며

관련 내용에 대해 궁금한 점이 있으시다면 언제든 편하게 질문해주세요.
