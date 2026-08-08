---
title: "[JAVA] SimpleDateFormat"
date: 2014-01-03 09:51:34 +0900
categories: ["프로그래밍", "JAVA"]
tags: []
---

> **[핵심 요약]**
> [JAVA] SimpleDateFormat 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트입니다.

---

## 1. 개요 및 배경

[JAVA] SimpleDateFormat과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유합니다.

---

## 2. 핵심 설명 및 코드

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

## 3. 정리하며

