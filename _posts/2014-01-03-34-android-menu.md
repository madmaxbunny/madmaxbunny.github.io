---
title: "[Android] Menu"
date: 2014-01-03 08:58:45 +0900
categories: ["프로그래밍", "Android"]
tags: []
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
    
