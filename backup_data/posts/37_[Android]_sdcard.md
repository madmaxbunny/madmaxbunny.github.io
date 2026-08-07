---
title: "[Android] sdcard"
date: "2014-01-03T09:05:02+09:00"
category: "프로그래밍/Android"
tags: []
original_url: "https://priv.tistory.com/37"
tistory_id: 37
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
    
