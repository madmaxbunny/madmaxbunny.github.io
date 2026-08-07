---
title: "Docker"
date: "2022-10-22T00:07:49+09:00"
category: "프로그래밍/System"
tags: ["docker"]
original_url: "https://priv.tistory.com/113"
tistory_id: 113
---

![](../images/img_113_01.png)

### 1\. 도커 레파지토리 등록
    
    
    ```bash
    yum install -y yum-utils
    yum-config-manager \
        --add-repo \
        https://download.docker.com/linux/centos/docker-ce.repo
    ```
    

### 2\. 도커 설치
    
    
    ```bash
    yum install docker-ce docker-ce-cli containerd.io
    systemctl start docker
    systemctl enable docker
    ```
    

### 3\. 도커 버전 확인
    
    
    ```bash
    docker version
    docker -v
    ```
    

### 4\. 도커 이미지 pull

<https://hub.docker.com/>
    
    
    ```bash
    docker pull httpd
    ```
    

### 5\. 이미지 확인
    
    
    ```bash
    docker images
    ```
    

### 6\. 도커 실행
    
    
    ```bash
    docker run httpd
    docker run --name ws2 httpd # 하나의 이미지로 또 다른 ws2라는 이름의 도커 실행 가능
    docker run -p 8000:80 httpd # 8000 → 80포트 포워딩
    ```
    

### 7\. 도커 확인
    
    
    ```bash
    docker ps
    docker ps -a # Stop 도커도 조회
    docker ps --no-trunc # ... 없이 ps 결과 보기
    ```
    

### 8\. 도커 중지
    
    
    ```bash
    dokcer stop ws2
    dokcer stop <Names>
    dokcer stop <Container ID>
    ```
    

### 9\. (중지했던) 도커 실행
    
    
    ```bash
    docker start <Container ID>
    ```
    

#### 

#### 9\. 도커 로그 보기 (중지했던 도커를 다시 실행할 경우 로그가 보이지 않기 때문에 아래 명령어 필요)
    
    
    ```bash
    docker logs -f ws2
    ```
    

### 10\. 도커 프로세스 삭제
    
    
    ```bash
    docker rm ws2		# Stop 상태의 도커만 삭제 가능
    docker rm --force ws2 	#실행중인 도커 삭제하기
    ```
    

### 11\. 도커 이미지 삭제
    
    
    ```bash
    docker rmi <IMAGE ID>
    ```
    

### 12\. 도커 커멘드 실행
    
    
    ```bash
    docker exec -it <name> /bin/sh 	#지원하는 이미지에 따라 /bin/bash 가능
    docker exec -it quirky_keller /bin/sh
    ```
    

### 13\. 도커 상세 정보 보기
    
    
    ```bash
    docker inspect <container_name>
    ```
    

* * *

### 스트링 부트

#### 1\. 스트링 부트 Maven 빌드
    
    
    ```bash
    ./mvnw package
    java -jar target/<jar>
    ```
    

#### 2\. Dockerfile 생성
    
    
    ```bash
    FROM openjdk:8-jdk-alpine
    ARG JAR_FILE=target/*.jar
    COPY ${JAR_FILE} app.jar
    ENTRYPOINT ["java","-jar","/app.jar"]
    ```
    

#### 3\. 이미지 생성
    
    
    ```bash
    docker build -t springio/gs-spring-boot-docker .
    ```
    

### 4\. 실행
    
    
    ```bash
    docker run -p 8080:8080 springio/gs-spring-boot-docker
    docker run --rm -d -p 8080:8080 springio/gs-spring-boot-docker 
    # --rm : 컨테이너를 stop하면 자동으로 컨테이너를 죽인다.
    # -d : 백그라운드 실행
    ```
    

<https://spring.io/guides/gs/spring-boot-docker/>

<https://perfectacle.github.io/2019/04/16/spring-boot-docker-image-optimization/>

* * *

### MYSQL
    
    
    ```bash
    docker pull mysql
    docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=<password> -d -p 3306:3306 mysql:latest
    docker exec -it mysql-container bash
    
    > mysql -u root -p
    ```
    

### GITLAB
    
    
    ```bash
    docker run
    --detach
    --hostname 도메인주소
    --publish 443:443
    --publish 80:80
    --publish 8022:22
    --name gitlab
    --restart always
    --volume $GITLAB_HOME/config:/etc/gitlab
    --volume $GITLAB_HOME/logs:/var/log/gitlab
    --volume $GITLAB_HOME/data:/var/opt/gitlab
    --volume $GITLAB_HOME/ssl:/etc/gitlab/ssl
    --shm-size 1024m
    docker-registry.cloud.hyundai-autoever.com/gitlab/gitlab-ce:latest
    ```
    
