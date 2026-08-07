---
title: "[Android] callback button"
date: "2014-01-03T09:06:48+09:00"
category: "프로그래밍/Android"
tags: []
original_url: "https://priv.tistory.com/38"
tistory_id: 38
---


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
    
