---
title: '[System] 안드로이드 폰에 우분투(Ubuntu) 설치하기'
date: 2014-01-03 09:11:09 +0900
categories:
- 프로그래밍
- System
tags: []
---
> **[핵심 요약]**
> 안드로이드 스마트폰에 우분투(Ubuntu) 리눅스 환경을 커스텀 설치하고 쉘에 접속하는 구축 절차입니다.

---

## 1. 개요 및 배경

[System] 안드로이드 폰에 우분투(Ubuntu) 설치하기은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

## 2. 핵심 설명 및 코드

> [System] 안드로이드 폰에 우분투(Ubuntu) 설치하기의 기본 개념과 실무 적용 명령어를 

---

[System] 안드로이드 폰에 우분투(Ubuntu) 설치하기은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

> [System] 안드로이드 폰에 우분투(Ubuntu) 설치하기 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트입니다.

---

[System] 안드로이드 폰에 우분투(Ubuntu) 설치하기과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유합니다.

---

타겟단말 : 겔럭시 S  
우분투 버전 : 12.04  
  
**1\. VMPlayer 및 Ubuntu 설치**  
[ _[System] 우분투(Ubuntu) 설치_](http://priv.tistory.com/41)  
  
  
**2. Ubuntu 이미지 만들기**  
$wget http://launchpadlibrarian.net/52888742/rootstock_0.1.99.4-0ubuntu1_i386.deb  
$sudo apt-get install qemu-kvm-extras-static qemu-kvm-extras debootstrap fuseext2 fuse-utils genext2fs  
$sudo dpkg -i rootstock_0.1.99.4-0ubuntu1_i386.deb  
 _(만약 failed to run command `debootstrap/debootstrap 과 관련된 메시지가 나온다면, fakeroot 설치 _  
_$sudo apt-get install fakeroot)_  
  
$sudo apt-get install fakeroot  
  
$dd if=/dev/zero of=ubuntu.img bs=1MB count=0 seek=2048  
$mke2fs -F ubuntu.img  
$sudo mount -o loop ubuntu.img /mnt  
$sudo tar -C /mnt -zxf armel-rootfs-*.tgz   
(만약 armel-rootfs~.tgz 파일이 만들어 지지 않는다면, 위에 밑줄 친 rootstock에서 오타가 있는지 확인할 것)  
  
  
**3\. 안드로이드폰 루팅하기**  
(참고 : [_http://dodoblog000.tistory.com/2_](http://dodoblog000.tistory.com/2))  
**  
  
****4\. 안드로이드 폰에 Ununtu 설치를 위한 애플리케이션 설치**  
4-1) Android Terminal Emulator  
\- 안드로이드 폰 상에서 Terminal 사용을 지원한다.  
  
4-2) Root Explorer  
\- 파일 탐색기 및 파일 권한 변경을 지원한다.  
  
  
**5\. 안드로이드 폰에****Ubuntu****이미지 복사**  
****

[![](/assets/img/posts/img_40_01.gif) bootubuntu](https://t1.daumcdn.net/cfile/tistory/271F404352C6000023)

**  
**5-1) 첨부한 bootubuntu 파일을 /system/bin 디렉토리에 복사한다.  
(다운받은 파일에 .txt 라는 확장자가 있다면 지워줄 것)  
5-2) 디렉토리의 권한을 755로 수정한다.  
5-3) /mnt/sdcard/ubuntu 디렉토리 생성한다.  
5-4) '**2.** Ubuntu**이미지 만들기'** 과정에서 만든 ubuntu.img 파일을 /mnt/sdcard/ubuntu로 복사한다.  
  
**6. Ubuntu 실행**  
Android Terminal Emulator 애플리케이션을 실행한다.   
$ su  
# bootubuntu  
  
  
**7\. DNS 설정**  
우분투에 네트워크는 잡혀 있는데 네임서버가 설정되어 있지 않는 경우, apt-get을 사용하면 오류가 발생할 수 있다.   
7-1) Ubuntu 처음 설치 시 네임서버가 127.0.0.1로 되어있어 아래와 같이 수정한다.  
$sudo nano /etc/resolv.conf  
nameserver 'DNS IP주소' 추가  
  
참고) 각 통신사 DNS  
SK : 219.250.36.130, 210.220.163.82  
KT : 168.126.63.1, 168.126.63.2  
LG : 164.124.107.9, 203.248.242.2  
구글 : 8.8.8.8, 8.8.4.4  
  
7-2) 네트워크 재시작  
$sudo /etc/init.d/networking restart  
  
7-3) 테스트  
$host naver.com  
  
7-4) 만약, 재부팅시 변경된 DNS가 다시 초기화 된다면 '7-1'말고 아래를 수행해 볼 것  
$sudo nano /etc/resolvconf/resolv.conf.d/head  
nameserver 'DNS IP주소' 추가  
(참고 : [_http://j4ckp4rd.tistory.com/32_](http://j4ckp4rd.tistory.com/32))  
  
**8\. 기타 업데이트**  
$apt-get update  
$apt-get upgrade  
$apt-get install gcc  
$apt-get install vim  
  
**9\. Helloworld 작성, 컴파일 및 실행**  
  
  
참조 : [_http://www.zdnet.co.kr/column/column_view.asp?artice_id=20120518070549_](http://www.zdnet.co.kr/column/column_view.asp?artice_id=20120518070549)  
참조 : [_http://blog.naver.com/nannomad?Redirect=Log &logNo=130159731508_](http://blog.naver.com/nannomad?Redirect=Log&logNo=130159731508)  
참조 : [_http://rayzie.tistory.com/48#recentComments_](http://rayzie.tistory.com/48#recentComments)

---

---

이상으로 [System] 안드로이드 폰에 우분투(Ubuntu) 설치하기의 기초 개념과 실행 방법에 대한 공유를 마칩니다.

---

## 3. 정리하며

이상으로 [System] 안드로이드 폰에 우분투(Ubuntu) 설치하기의 기초 개념과 실행 방법에 대한 공유를 마칩니다.