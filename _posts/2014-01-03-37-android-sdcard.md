---
title: "[Android] sdcard"
date: 2014-01-03 09:05:02 +0900
categories: ["프로그래밍", "Android"]
tags: []
---

> 💡 **TL;DR (핵심 요약)**  
> [Android] sdcard에 대한 상세 설명 및 핵심 가이드입니다.

---

## 1. 개요 및 배경

[Android] sdcard 가이드 및 실무 적용 설명입니다.

---

## 2. 핵심 설정 및 실행 가이드

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

## 3. 요약 및 참고사항

- 본 포스트는 실무 개발 및 인프라 운용 중 검증된 노하우를 바탕으로 정리되었습니다.
- 추가 문의나 개선사항은 포스트 하단 댓글 또는 GitHub 이슈로 전달해 주세요.
