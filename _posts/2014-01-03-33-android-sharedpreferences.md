---
title: "[Android] SharedPreferences"
date: 2014-01-03 08:54:18 +0900
categories: ["프로그래밍", "Android"]
tags: []
---

> 💡 **TL;DR (핵심 요약)**  
> [Android] SharedPreferences에 대한 상세 설명 및 핵심 가이드입니다.

---

## 1. 개요 및 배경

[Android] SharedPreferences 가이드 및 실무 적용 설명입니다.

---

## 2. 핵심 설정 및 실행 가이드

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

## 3. 요약 및 참고사항

- 본 포스트는 실무 개발 및 인프라 운용 중 검증된 노하우를 바탕으로 정리되었습니다.
- 추가 문의나 개선사항은 포스트 하단 댓글 또는 GitHub 이슈로 전달해 주세요.
