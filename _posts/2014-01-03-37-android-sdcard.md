---
title: '[Android] sdcard'
date: 2014-01-03 09:05:02 +0900
categories:
- 프로그래밍
- Android
tags: []
---
> **[핵심 요약]**
> 안드로이드 외부 저장소(SD 카드) 경로를 조회하고 파티션에 파일 읽기/쓰기를 수행하는 코드입니다.

---

## 1. 개요 및 배경

[Android] sdcard은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

## 2. 핵심 설명 및 코드

> [Android] sdcard의 기본 개념과 실무 적용 명령어를 

---

[Android] sdcard은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

> [Android] sdcard 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트입니다.

---

[Android] sdcard과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유합니다.

---

```

package kr.priv.android_sdcard; 
  
import java.io.File; 
import java.util.ArrayList; 
import java.util.List; 
  
import android.app.Activity; 
import android.os.Bundle; 
import android.os.Environment; 
import android.util.Log; 
import android.view.Menu; 
import android.widget.ArrayAdapter; 
import android.widget.ListView; 
  
public class AT_main extends Activity { 
  
List mFileNames = new ArrayList(); 
  
@Override
public void onCreate(Bundle savedInstanceState) { 
super.onCreate(savedInstanceState); 
  
ListView listview = new ListView(this); 
  
setContentView(listview); 
String root = Environment.getExternalStorageDirectory().getAbsolutePath(); 
// + File.separator + "sbin" + File.separator; 
File f = new File(root); 
  
  
for (File file : f.listFiles()) { 
    mFileNames.add(file.getName()); 
} 
  
ArrayAdapter adapter = new ArrayAdapter(this, 
        android.R.layout.simple_list_item_1, mFileNames); 
listview.setAdapter(adapter); 
} 
  
@Override
public boolean onCreateOptionsMenu(Menu menu) { 
getMenuInflater().inflate(R.menu.main, menu); 
return true; 
} 
  
}

```
    
    
    
```

 
  
 
  
 
  

```
    
    
    
```

 
 

```

---

---

이상으로 [Android] sdcard의 기초 개념과 실행 방법에 대한 공유를 마칩니다.

---

## 3. 정리하며

이상으로 [Android] sdcard의 기초 개념과 실행 방법에 대한 공유를 마칩니다.