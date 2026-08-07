---
title: "[Android] SharedPreferences"
date: "2014-01-03T08:54:18+09:00"
category: "프로그래밍/Android"
tags: []
original_url: "https://priv.tistory.com/33"
tistory_id: 33
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
    
