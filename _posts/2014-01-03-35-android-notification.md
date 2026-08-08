---
title: "[Android] Notification"
date: 2014-01-03 08:59:42 +0900
categories: ["프로그래밍", "Android"]
tags: []
---

> **[핵심 요약]**
> [Android] Notification 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트입니다.

---

## 1. 개요 및 배경

[Android] Notification과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유합니다.

---

## 2. 핵심 설명 및 코드

```

        Notification notification = new Notification(R.drawable.ic_launcher, getText(R.string.app_name), System.currentTimeMillis()); 
        Intent notificationIntent = new Intent(this, AT_main.class); 
        PendingIntent pendingIntent = PendingIntent.getActivity(this, 0, notificationIntent, 0); 
        notification.setLatestEventInfo(this, "test", "test2", pendingIntent); 
        startForeground(12345, notification);

```

---

## 3. 정리하며

관련해서 궁금하신 점이나 나눠보고 싶은 의견이 있다면 댓글로 편하게 남겨주시기 바랍니다.
