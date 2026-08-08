---
title: "[System] 우분투(Ubuntu) 설치"
date: 2014-01-03 09:16:50 +0900
categories: ["프로그래밍", "System"]
tags: []
---

> 💡 **TL;DR (핵심 요약)**  
> [System] 우분투(Ubuntu) 설치에 대한 상세 설명 및 핵심 가이드입니다.

---

## 1. 개요 및 배경

[System] 우분투(Ubuntu) 설치 가이드 및 실무 적용 설명입니다.

---

## 2. 핵심 설정 및 실행 가이드

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

## 3. 요약 및 참고사항

- 본 포스트는 실무 개발 및 인프라 운용 중 검증된 노하우를 바탕으로 정리되었습니다.
- 추가 문의나 개선사항은 포스트 하단 댓글 또는 GitHub 이슈로 전달해 주세요.
