---
title: "[Android] SharedPreferences"
date: 2014-01-03 08:54:18 +0900
categories: ["프로그래밍", "Android"]
tags: []
---

> **[핵심 요약]**
> [Android] SharedPreferences 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트이에요.

---

## 1. 개요 및 배경

[Android] SharedPreferences과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유해요.

---

## 2. 핵심 설명 및 코드

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

## 3. 정리하며

관련해서 궁금하신 점이나 나눠보고 싶은 의견이 있다면 댓글로 편하게 말씀해주세요.
