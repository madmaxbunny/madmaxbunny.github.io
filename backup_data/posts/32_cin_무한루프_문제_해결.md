---
title: "cin 무한루프 문제 해결"
date: "2010-02-25T16:06:09+09:00"
category: "프로그래밍/C/C++"
tags: ["CIN", "루프", "무한"]
original_url: "https://priv.tistory.com/32"
tistory_id: 32
---


    ```
         
    do{
      cout<<"원하는 매뉴의 번호를 입력하십시오";
      cin>>inPutNum;
     
      itoa(inPutNum,charNum,10);
    
     if(MY_IsNumber(charNum)) continue; // num이 숫자이면 1을 리턴
     
     }while(inPutNum < fn || inPutNum > en);
    
    ```
    
