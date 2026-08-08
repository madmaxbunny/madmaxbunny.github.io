---
title: '[System] 우분투(Ubuntu) 설치'
date: 2014-01-03 09:16:50 +0900
categories:
- 프로그래밍
- System
tags: []
---
> **[핵심 요약]**
> VMware 가상 머신 상에 우분투(Ubuntu) 리눅스 OS를 설치하고 네트워크 및 기본 환경을 구축하는 노하우입니다.

---

## 1. 개요 및 배경

[System] 우분투(Ubuntu) 설치은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

## 2. 핵심 설명 및 코드

> [System] 우분투(Ubuntu) 설치의 기본 개념과 실무 적용 명령어를 

---

[System] 우분투(Ubuntu) 설치은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

> [System] 우분투(Ubuntu) 설치 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트입니다.

---

[System] 우분투(Ubuntu) 설치과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유합니다.

---

**1\. VMPlayer 다운로드**  
[ _https://my.vmware.com/web/vmware/free#desktop_end_user_computing/vmware_player/5_0_](https://my.vmware.com/web/vmware/free#desktop_end_user_computing/vmware_player/5_0)  
**  
**2.****우분투 다운로드****  
[ _http://www.ubuntu.com/download/desktop_](http://www.ubuntu.com/download/desktop)  
  
**3\. 우분투 설치 진행 시, 아래화면에 적는 것이 계정이름과 로그인 암호가 된다.**

![](/assets/img/posts/img_41_01.png)

**  
**  
  
**4\. root 계정 암호 설정**  
sudo passwd root  
  
**5\. X-Window 설치**  
sudo apt-get install xinit  
sudo apt-get update  
sudo apt-get upgrade  
sudo apt-get install ubuntu-desktop  
startx  
  
**6\. Terminal 창의 위치**  
****

![](/assets/img/posts/img_41_02.png)

**  
**  
**7\. VMware Tool 설치(아래 그림은 설치 후, 화면)**  
****

![](/assets/img/posts/img_41_03.png)

**  
**

---

---

이상으로 [System] 우분투(Ubuntu) 설치의 기초 개념과 실행 방법에 대한 공유를 마칩니다.

---

## 3. 정리하며

이상으로 [System] 우분투(Ubuntu) 설치의 기초 개념과 실행 방법에 대한 공유를 마칩니다.