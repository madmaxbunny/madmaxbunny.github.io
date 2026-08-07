---
title: "[UNIX] makefile"
date: "2014-01-03T09:43:18+09:00"
category: "프로그래밍/System"
tags: []
original_url: "https://priv.tistory.com/46"
tistory_id: 46
---


    ```
    msh : libmsh.o msh_main.o 
     gcc -o msh libmsh.o msh_main.o 
    libmsh.o : libmsh.c libmsh.h 
     gcc -c libmsh.c 
    msh_main.o : libmsh.c libmsh.h 
     gcc -c msh_main.c 
    clean: 
     rm *.o
    
    ```
    

Eaxmple 
    
    
    ```
    dstest : mylist.o myqueue.o member_info.o stock_reserv.o dstest_main.o 
     gcc -o dstest mylist.o myqueue.o member_info.o stock_reserv.o dstest_main.o 
    mylist : mylist.c mylist.h 
     gcc -c dstest_main.c 
    myqueue : myqueue.c myqueue.h 
     gcc -c myqueue.c 
    member_info : member_info.c member_info.h 
     gcc -c member_info.c 
    stock_reserv : stock_reserv.c stock_reserv.h 
     gcc -c stock_reserv.c 
    dstest_main : dstest_main.c stock_reserv.h member_info.h myqueue.c mylist.h 
     gcc -c dstest_main.c 
    clean :   
     rm *.o
    
    ```
    
