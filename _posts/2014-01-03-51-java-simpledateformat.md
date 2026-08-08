---
title: "[JAVA] SimpleDateFormat"
date: 2014-01-03 09:51:34 +0900
categories: ["프로그래밍", "JAVA"]
tags: []
---

> 💡 **TL;DR (핵심 요약)**  
> [JAVA] SimpleDateFormat에 대한 상세 설명 및 핵심 가이드입니다.

---

## 1. 개요 및 배경

[JAVA] SimpleDateFormat 가이드 및 실무 적용 설명입니다.

---

## 2. 핵심 설정 및 실행 가이드

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

## 3. 요약 및 참고사항

- 본 포스트는 실무 개발 및 인프라 운용 중 검증된 노하우를 바탕으로 정리되었습니다.
- 추가 문의나 개선사항은 포스트 하단 댓글 또는 GitHub 이슈로 전달해 주세요.
