---
title: "[System] 우분투(Ubuntu) 설치"
date: 2014-01-03 09:16:50 +0900
categories: ["프로그래밍", "System"]
tags: []
---

> **[핵심 요약]**
> [System] 우분투(Ubuntu) 설치 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트이에요.

---

## 1. 개요 및 배경

[System] 우분투(Ubuntu) 설치과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유해요.

---

## 2. 핵심 설명 및 코드

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

## 3. 정리하며

관련해서 궁금하신 점이나 나눠보고 싶은 의견이 있다면 댓글로 편하게 말씀해주세요.
