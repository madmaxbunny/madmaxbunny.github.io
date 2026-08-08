---
title: '[Android] Notification'
date: 2014-01-03 08:59:42 +0900
categories:
- 프로그래밍
- Android
tags: []
---

[Android] Notification에 대한 정리 노트이에요. 참고하시는 데 도움되었으면 해요.

---

## 개요 및 배경

[Android] Notification에 관해 실무와 개발 과정에서 알게 된 핵심 내용들을 공유해요.

---

## 핵심 설명 및 코드

>  **TL;DR (핵심 요약)**  
> [Android] Notification에 대한 상세 설명 및 핵심 가이드이에요.

---

## 개요 및 배경

[Android] Notification 가이드 및 실무 적용 설명이에요.

---

## 핵심 설명 및 코드

```
    
            Notification notification = new Notification(R.drawable.ic_launcher, getText(R.string.app_name), System.currentTimeMillis()); 
            Intent notificationIntent = new Intent(this, AT_main.class); 
            PendingIntent pendingIntent = PendingIntent.getActivity(this, 0, notificationIntent, 0); 
            notification.setLatestEventInfo(this, "test", "test2", pendingIntent); 
            startForeground(12345, notification);
    
    ```

---

## 정리하며

- 본 포스트는 실무 개발 및 인프라 운용 중 검증된 노하우를 바탕으로 정리되었습니다.
- 추가 문의나 개선사항은 포스트 하단 댓글 또는 GitHub 이슈로 전달해 주세요.

---

## 정리하며

관련 내용에 대해 궁금한 점이 있으시다면 언제든 편하게 질문해주세요.
