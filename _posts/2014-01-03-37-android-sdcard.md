---
title: "[Android] sdcard"
date: 2014-01-03 09:05:02 +0900
categories: ["프로그래밍", "Android"]
tags: []
---

> **[핵심 요약]**
> [Android] sdcard 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트이에요.

---

## 1. 개요 및 배경

[Android] sdcard과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유해요.

---

## 2. 핵심 설명 및 코드

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

## 3. 정리하며

관련해서 궁금하신 점이나 나눠보고 싶은 의견이 있다면 댓글로 편하게 말씀해주세요.
