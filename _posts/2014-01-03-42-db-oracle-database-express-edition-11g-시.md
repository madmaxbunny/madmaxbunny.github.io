---
title: '[DB] Oracle Database Express Edition 11g 시작하기'
date: 2014-01-03 09:28:19 +0900
categories:
- 프로그래밍
- DB
tags: []
---
> **[핵심 요약]**
> Oracle Database Express Edition 11g 데이터베이스 설치 및 서비스 기동 설정 노트입니다.

---

## 1. 개요 및 배경

[DB] Oracle Database Express Edition 11g 시작하기은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

## 2. 핵심 설명 및 코드

> [DB] Oracle Database Express Edition 11g 시작하기의 기본 개념과 실무 적용 명령어를 

---

[DB] Oracle Database Express Edition 11g 시작하기은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

> [DB] Oracle Database Express Edition 11g 시작하기 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트입니다.

---

[DB] Oracle Database Express Edition 11g 시작하기과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유합니다.

---

**1\. Oracle Database Express Edition 11g 설치**  
\- [_http://www.oracle.com/technetwork/indexes/downloads/index.html_](http://www.oracle.com/technetwork/indexes/downloads/index.html) 에서 다운 가능하다.  
\- Express Edition는 무료버젼이며, 한 명의 uesr만 사용 가능하다.  
\- 다운 받기 위해 회원가입을 필요로한다.  
\- 설치버젼 : Oracle Database Express Edition 11g Release 2  
  
**2\. Oracle SQL Developer 실행  
** \- 마찬가지로 [_http://www.oracle.com/technetwork/indexes/downloads/index.html_](http://www.oracle.com/technetwork/indexes/downloads/index.html) 에서 다운 가능하다.  
\- 파일 다운로드 후, 압축을 풀고 설치없이 sqldeveloper.exe 를 실행하면 된다.  
\- 설치버젼 : sqldeveloper-3.2.10.09.57_Win32  
  
\- 만약 실행 시 아래와 같은 에러가 뜬다면, 메모리량이 부족하기 때문이다. 기본값은 2GB를 요구한다.  

![](/assets/img/posts/img_42_01.png)

  
\- 오류를 수정하기 위해 .. \sqldeveloper-3.2.10.09.57_Win32\sqldeveloper\sqldeveloper\bin\sqldeveloper.conf 을 열고  
하단 그림과 같이 'AddVMOption -Xmx256m' 문장을 추가하여 요구 메모리량을 256M로 수정한다.  
  

![](/assets/img/posts/img_42_02.png)

  
  
**3\. 실행 준비**  
  
\- 윈도우 시작 > 모든 프로그램 > Oracle Database 11g Express Edition > Run SQL Command Line을 실행해서  
아래 그림과 같이 계정의 lock해제 및 페스워드를 변경한다.   
\- 참고 [_http://blog.naver.com/190191?Redirect=Log &logNo=50086403055_](http://blog.naver.com/190191?Redirect=Log&logNo=50086403055)   

![](/assets/img/posts/img_42_03.png)

  
  
**4\. Oracle SQL Developer 실행  
** \- Oracle SQL Developer 실행시킨 후, 다음과 같이 작성할 수 있다. (비밀번호 : hr)  
\- 모두 입력이 끝났다면, 테스트 버튼을 눌러, 이상이 없는지 확인한다.   
(이상이 없다면 왼쪽 하단에 '성공' 메시지를 볼 수 있다.)  

![](/assets/img/posts/img_42_04.png)

  
  
  
**5\. 환경 설정**  
\- 상단의 도구 > 환경설정을 클릭한다.  
\- 글꼴 수정은 아래 그림과 같다.  

![](/assets/img/posts/img_42_05.png)

  
  
\- 라인넘버 보이는 방법은 아래와 같다.  

![](/assets/img/posts/img_42_06.png)

  
  
  
\- 포멧터 위치  

![](/assets/img/posts/img_42_07.png)

  
  
  
\- 다른 이름으로 저장을 눌러 원하는 이름을 입력한다. 편집 버튼을 눌러 원하는 포멧을 설정한다. (편집기에서 Ctrl + F7을 누르면 설정한 포멧으로 적용된다.)  
  

![](/assets/img/posts/img_42_08.png)

  
  
\- 백스페이스 안먹힐 때  
Tools > Preference > Accelerators > Load Preset > Default > OK  
  
\- 자동완성 기능 해제  
Tools > Preference > Code Editor > Code Insight > Enable... 전부 체크 해제  
  
\- 자동완성 기능 해제(한글버젼)  
도구 > 환경설정 > 코드 편집기 > 완성 인사이트 >  
SQL 워크시트에서 완성 자동 팝업 사용 체크 해제  
PL/SQL 편집기에서 완성 자동 팝업 사용 체크 해제  
  
\- 자동 완성 기능을 사용할 때, 타이핑 중인 단어가 완성되는 것이 아닌, 단어가 추가만 될 때가 있다.   
필자는 이것 때문에 자동 완성 기능을 지우려 했으나, 어찌된 일인지 설치 후 하루가 지나니 이러한 현상이 사라졌다.   
(프로그램 버그인듯..)

---

---

이상으로 [DB] Oracle Database Express Edition 11g 시작하기의 기초 개념과 실행 방법에 대한 공유를 마칩니다.

---

## 3. 정리하며

이상으로 [DB] Oracle Database Express Edition 11g 시작하기의 기초 개념과 실행 방법에 대한 공유를 마칩니다.