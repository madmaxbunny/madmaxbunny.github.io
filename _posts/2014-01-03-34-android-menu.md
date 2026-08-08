---
title: "[Android] Menu"
date: 2014-01-03 08:58:45 +0900
categories: ["프로그래밍", "Android"]
tags: []
---

> **[핵심 요약]**
> [Android] Menu 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트이에요.

---

## 1. 개요 및 배경

[Android] Menu과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유해요.

---

## 2. 핵심 설명 및 코드

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

## 3. 정리하며

관련해서 궁금하신 점이나 나눠보고 싶은 의견이 있다면 댓글로 편하게 말씀해주세요.
