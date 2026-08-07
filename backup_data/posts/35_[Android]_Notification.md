---
title: "[Android] Notification"
date: "2014-01-03T08:59:42+09:00"
category: "프로그래밍/Android"
tags: []
original_url: "https://priv.tistory.com/35"
tistory_id: 35
---


    ```
    
            Notification notification = new Notification(R.drawable.ic_launcher, getText(R.string.app_name), System.currentTimeMillis()); 
            Intent notificationIntent = new Intent(this, AT_main.class); 
            PendingIntent pendingIntent = PendingIntent.getActivity(this, 0, notificationIntent, 0); 
            notification.setLatestEventInfo(this, "test", "test2", pendingIntent); 
            startForeground(12345, notification);
    
    ```
    
