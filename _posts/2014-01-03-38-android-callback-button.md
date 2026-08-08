---
title: "[Android] callback button"
date: 2014-01-03 09:06:48 +0900
categories: ["프로그래밍", "Android"]
tags: []
---

> **[핵심 요약]**
> [Android] callback button 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트이에요.

---

## 1. 개요 및 배경

[Android] callback button과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유해요.

---

## 2. 핵심 설명 및 코드

```

package kr.priv; 
  
import android.app.Activity; 
import android.os.Bundle; 
import android.widget.TextView; 
  
public class Test_handler_btnActivity extends Activity { 
    TextView show; 
    @Override
    public void onCreate(Bundle savedInstanceState) { 
        super.onCreate(savedInstanceState); 
        setContentView(R.layout.main); 
          
        MD_test test = new MD_test(); 
        show = (TextView)findViewById(R.id.show); 
          
        MD_test.OnReceiveResult callback = new MD_test.OnReceiveResult() { 
              
            @Override
            public void onReceiveStream(int timeStamp) { 
                // TODO Auto-generated method stub 
                show.setText(">"+timeStamp); 
                  
            } 
        }; 
          
        test.setOnReceiveResult(callback); 
          
          
    } 
}

```
    
    
    
```

package kr.priv; 
  
import android.os.Handler; 
import android.os.Message; 
  
public class MD_test { 
      
    interface OnReceiveResult { 
        void onReceiveStream(int timeStamp); 
    } 
  
    private OnReceiveResult mCallback; 
  
    public void setOnReceiveResult(OnReceiveResult callback) { 
        mCallback = callback; 
        ServerModeThread tread = new ServerModeThread(); 
        tread.start(); 
    } 
  
    int cnt = 0; 
    private class ServerModeThread extends Thread { 
        public void run(){ 
              
            while (true) { 
                try { 
                      
                    handler.sendEmptyMessage(0); 
                    Thread.sleep(1000); 
                } catch (InterruptedException e) { 
                    // TODO Auto-generated catch block 
                    e.printStackTrace(); 
                } 
            } 
              
        } 
    } 
      
    Handler handler = new Handler() { 
        public void handleMessage(Message msg) { 
            if (msg.what == 0) { 
  
                cnt++; 
                mCallback.onReceiveStream(cnt); 
  
            } 
        } 
    }; 
}

```

---

## 3. 정리하며

관련해서 궁금하신 점이나 나눠보고 싶은 의견이 있다면 댓글로 편하게 말씀해주세요.
