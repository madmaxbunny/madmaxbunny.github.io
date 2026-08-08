---
title: '[Android] callback button'
date: 2014-01-03 09:06:48 +0900
categories:
- 프로그래밍
- Android
tags: []
---

[Android] callback button에 대한 정리 노트이에요. 참고하시는 데 도움되었으면 해요.

---

## 개요 및 배경

[Android] callback button에 관해 실무와 개발 과정에서 알게 된 핵심 내용들을 공유해요.

---

## 핵심 설명 및 코드

>  **TL;DR (핵심 요약)**  
> [Android] callback button에 대한 상세 설명 및 핵심 가이드이에요.

---

## 개요 및 배경

[Android] callback button 가이드 및 실무 적용 설명이에요.

---

## 핵심 설명 및 코드

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

## 정리하며

- 본 포스트는 실무 개발 및 인프라 운용 중 검증된 노하우를 바탕으로 정리되었습니다.
- 추가 문의나 개선사항은 포스트 하단 댓글 또는 GitHub 이슈로 전달해 주세요.

---

## 정리하며

관련 내용에 대해 궁금한 점이 있으시다면 언제든 편하게 질문해주세요.
