---
title: "[Android] Menu"
date: 2014-01-03 08:58:45 +0900
categories: ["프로그래밍", "Android"]
tags: []
---

> 💡 **TL;DR (핵심 요약)**  
> [Android] Menu에 대한 상세 설명 및 핵심 가이드입니다.

---

## 1. 개요 및 배경

[Android] Menu 가이드 및 실무 적용 설명입니다.

---

## 2. 핵심 설정 및 실행 가이드

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

## 3. 요약 및 참고사항

- 본 포스트는 실무 개발 및 인프라 운용 중 검증된 노하우를 바탕으로 정리되었습니다.
- 추가 문의나 개선사항은 포스트 하단 댓글 또는 GitHub 이슈로 전달해 주세요.
