---
title: '[Android] SharedPreferences'
date: 2014-01-03 08:54:18 +0900
categories:
- 프로그래밍
- Android
tags: []
---
> **[핵심 요약]**
> 안드로이드 앱에서 키-값(Key-Value) 형태로 환경 설정 데이터를 영구 저장하는 SharedPreferences 사용법입니다.

---

## 1. 개요 및 배경

[Android] SharedPreferences은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

## 2. 핵심 설명 및 코드

> [Android] SharedPreferences의 기본 개념과 실무 적용 명령어를 

---

[Android] SharedPreferences은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

> [Android] SharedPreferences 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트입니다.

---

[Android] SharedPreferences과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유합니다.

---

```
private void getPreferences() { 
SharedPreferences pref = getSharedPreferences("pref", MODE_PRIVATE); 
String a = pref.getString("key1", ""); 
Toast.makeText(this, a, 0).show(); 
} 
  
// 값 저장하기 
private void savePreferences() { 
SharedPreferences pref = getSharedPreferences("pref", MODE_PRIVATE); 
SharedPreferences.Editor editor = pref.edit(); 
editor.putString("key1", "data"); 
editor.commit(); 
} 
  
// 값(Key Data) 삭제하기 
private void removePreferences() { 
SharedPreferences pref = getSharedPreferences("pref", MODE_PRIVATE); 
SharedPreferences.Editor editor = pref.edit(); 
editor.remove("key1"); 
editor.commit(); 
} 
  
// 값(ALL Data) 삭제하기 
private void removeAllPreferences() { 
SharedPreferences pref = getSharedPreferences("pref", MODE_PRIVATE); 
SharedPreferences.Editor editor = pref.edit(); 
editor.clear(); 
editor.commit(); 
}

```
    

Activity가 아닌 다른 class에서 사용하려면, context만 넘겨주면 된다 
    
    
```

SharedPreferences pref = mContext.getSharedPreferences("pref", MODE_PRIVATE);

```

---

---

이상으로 [Android] SharedPreferences의 기초 개념과 실행 방법에 대한 공유를 마칩니다.

---

## 3. 정리하며

이상으로 [Android] SharedPreferences의 기초 개념과 실행 방법에 대한 공유를 마칩니다.