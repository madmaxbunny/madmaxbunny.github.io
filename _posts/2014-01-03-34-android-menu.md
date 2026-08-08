---
title: '[Android] Menu'
date: 2014-01-03 08:58:45 +0900
categories:
- 프로그래밍
- Android
tags: []
---
> **[핵심 요약]**
> 안드로이드 액티비티 메뉴 바에 옵션 메뉴(Option Menu)를 구성하고 클릭 이벤트를 처리하는 구현 코드입니다.

---

## 1. 개요 및 배경

[Android] Menu은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

## 2. 핵심 설명 및 코드

> [Android] Menu의 기본 개념과 실무 적용 명령어를 

---

[Android] Menu은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

> [Android] Menu 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트입니다.

---

[Android] Menu과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유합니다.

---

```

package kr.priv.logManagement; 
  
import android.app.Activity; 
import android.content.Intent; 
import android.os.Bundle; 
import android.view.Menu; 
import android.view.MenuItem; 
  
public class AT_main extends Activity { 
  
@Override
public void onCreate(Bundle savedInstanceState) { 
super.onCreate(savedInstanceState); 
setContentView(R.layout.layout_main);        
} 
  
@Override
public boolean onCreateOptionsMenu(Menu menu) { 
getMenuInflater().inflate(R.menu.layout_main, menu); 
return true; 
} 
  
public boolean onOptionsItemSelected(MenuItem item) { 
switch (item.getItemId()) { 
case R.id.menu_settings: 
    Intent intent = new Intent(this, AT_logManagement.class); 
    startActivity(intent); 
    return true; 
default: 
    return super.onOptionsItemSelected(item); 
} 
} 
  
  
}

```

---

---

이상으로 [Android] Menu의 기초 개념과 실행 방법에 대한 공유를 마칩니다.

---

## 3. 정리하며

이상으로 [Android] Menu의 기초 개념과 실행 방법에 대한 공유를 마칩니다.