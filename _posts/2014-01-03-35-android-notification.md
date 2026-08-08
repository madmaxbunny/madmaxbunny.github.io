---
title: '[Android] Notification'
date: 2014-01-03 08:59:42 +0900
categories:
- 프로그래밍
- Android
tags: []
---
> **[핵심 요약]**
> 안드로이드 상태바 알림(Notification) 메시지를 생성하고 터치 시 액티비티로 이동시키는 방법입니다.

---

## 1. 개요 및 배경

[Android] Notification은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

## 2. 핵심 설명 및 코드

> [Android] Notification의 기본 개념과 실무 적용 명령어를 

---

[Android] Notification은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

> [Android] Notification 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트입니다.

---

[Android] Notification과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유합니다.

---

```

Notification notification = new Notification(R.drawable.ic_launcher, getText(R.string.app_name), System.currentTimeMillis()); 
Intent notificationIntent = new Intent(this, AT_main.class); 
PendingIntent pendingIntent = PendingIntent.getActivity(this, 0, notificationIntent, 0); 
notification.setLatestEventInfo(this, "test", "test2", pendingIntent); 
startForeground(12345, notification);

```

---

---

이상으로 [Android] Notification의 기초 개념과 실행 방법에 대한 공유를 마칩니다.

---

## 3. 정리하며

이상으로 [Android] Notification의 기초 개념과 실행 방법에 대한 공유를 마칩니다.