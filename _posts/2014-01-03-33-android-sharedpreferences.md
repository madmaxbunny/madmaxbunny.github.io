---
title: '[Android] SharedPreferences'
date: 2014-01-03 08:54:18 +0900
categories:
- 프로그래밍
- Android
tags: []
---

> **[핵심 요약]**
> [Android] SharedPreferences 작업에 대해 실무에서 검증된 핵심 설정 및 처리 방법을 정돈해둔 노트이에요.

---

## 1. 개요 및 배경

[Android] SharedPreferences에 관해 개발 및 인프라 운용 과정에서 접했던 내용들을 공유해볼게요.

---

## 2. 핵심 설명 및 설정 가이드

---

## 1. 개요 및 배경

---

## 2. 핵심 설명 및 설정 가이드

>  **TL;DR (핵심 요약)**  
> [Android] SharedPreferences에 대한 상세 설명 및 핵심 가이드이에요.

---

## 1. 개요 및 배경

[Android] SharedPreferences 가이드 및 실무 적용 설명이에요.

---

## 2. 핵심 설명 및 설정 가이드

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

- 본 포스트는 실무 개발 및 인프라 운용 중 검증된 노하우를 바탕으로 정리되었습니다.
- 추가 문의나 개선사항은 포스트 하단 댓글 또는 GitHub 이슈로 전달해 주세요.

---

## 3. 정리하며

관련 내용에 대해 궁금한 점이 있으시다면 언제든 편하게 질문해주세요.

---

## 3. 정리하며

관련해서 궁금하신 점이나 나눠보고 싶은 의견이 있으시다면 언제든 댓글로 편하게 말씀해주세요.
