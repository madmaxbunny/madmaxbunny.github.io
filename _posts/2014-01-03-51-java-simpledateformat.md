---
title: '[JAVA] SimpleDateFormat'
date: 2014-01-03 09:51:34 +0900
categories:
- 프로그래밍
- JAVA
tags: []
---
> **[핵심 요약]**
> [JAVA] SimpleDateFormat의 기본 개념과 실무 적용 명령어를 대학교 1학년 눈높이에 맞춰 정리한 기술 노트입니다.

---

## 1. 개요 및 배경

[JAVA] SimpleDateFormat은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 초보자 분들도 쉽게 이해할 수 있도록 기본 용어 개념과 배경 지식을 먼저 설명하고, 실제 적용 코드와 실행법을 차근차근 다룹니다.

---

## 2. 핵심 설명 및 코드

> [JAVA] SimpleDateFormat의 기본 개념과 실무 적용 명령어를 대학교 1학년 눈높이에 맞춰 정리한 기술 노트입니다.

---

[JAVA] SimpleDateFormat은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 초보자 분들도 쉽게 이해할 수 있도록 기본 용어 개념과 배경 지식을 먼저 설명하고, 실제 적용 코드와 실행법을 차근차근 다룹니다.

---

> [JAVA] SimpleDateFormat 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트입니다.

---

[JAVA] SimpleDateFormat과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유합니다.

---

```

import java.text.SimpleDateFormat; 
import java.util.Date; 
import java.util.Calendar; 
import java.util.TimeZone; 
  
public class test { 
public static void main(String[] args) { 
  
System.out.println(getCurrentDateTime()); 
} 
  
static String getCurrentDateTime() { 
SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss.ms"); 
Date dateTime = new Date(); 
TimeZone tz = TimeZone.getTimeZone("Asia/Seoul"); 
sdf.setTimeZone(tz); 
  
return sdf.format(dateTime); 
} 
}

```

---

---

이상으로 [JAVA] SimpleDateFormat의 기초 개념과 실행 방법에 대한 공유를 마칩니다.

---

## 3. 정리하며

이상으로 [JAVA] SimpleDateFormat의 기초 개념과 실행 방법에 대한 공유를 마칩니다.
