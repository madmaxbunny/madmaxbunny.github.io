---
title: "Queue"
date: "2010-01-09T14:55:11+09:00"
category: "프로그래밍/Data Structure"
tags: ["Queue"]
original_url: "https://priv.tistory.com/22"
tistory_id: 22
---

#include <stdio.h>  
#include <string.h>  
#define QUESIZ 5

void enqueue(char*,int*,int*,char);  
char dequeue(char*,int*,int*);  
void printQueue(char*,int*,int*); // 큐 내용 출력

void main(){

char queue[QUESIZ+1]; // 큐  
int fr=0, rr=0; // 큐 포인터   
  
enqueue(queue,&fr,&rr,'2');  
//printf("<%s>\n",queue);   
enqueue(queue,&fr,&rr,'0');  
enqueue(queue,&fr,&rr,'0');  
enqueue(queue,&fr,&rr,'6');  
enqueue(queue,&fr,&rr,'5');  
printf("\n");  
printQueue(queue,&fr,&rr); // 큐 내용 출력  
printf("------------\n");  
  
dequeue(queue,&fr,&rr);  
dequeue(queue,&fr,&rr);  
dequeue(queue,&fr,&rr);  
dequeue(queue,&fr,&rr);  
dequeue(queue,&fr,&rr);

  
enqueue(queue,&fr,&rr,'1');  
printQueue(queue,&fr,&rr); // 큐 내용 출력  
  
enqueue(queue,&fr,&rr,'2');  
printQueue(queue,&fr,&rr); // 큐 내용 출력  
  
dequeue(queue,&fr,&rr);  
enqueue(queue,&fr,&rr,'3');  
printQueue(queue,&fr,&rr); // 큐 내용 출력  
  
enqueue(queue,&fr,&rr,'4');  
printQueue(queue,&fr,&rr); // 큐 내용 출력  
  
printf("\n\n");

}

int modAdd(int a){

return (a+1) % (QUESIZ+1);  
}

void enqueue(char *queue, int *fr, int *rr, char data){  
  
if(*fr == modAdd(*rr)){ //[예외처리]Queue가 가득차면   
printf("queue is full!\n"); //error 메세지   
return;  
}  
  
printf("enuque[%c]!\n",data);  
queue[*rr] = data;  
*rr = modAdd(*rr);

printf("<%s>\n",queue);   
}

char dequeue(char *queue, int *fr, int *rr){

char data;  
if(*fr == *rr){  
printf("queue is empty!\n");  
return 0;  
}  
  
data = queue[*fr];  
*fr = modAdd(*fr);

printf("\ndelete[%c]!\n",data);  
printQueue(queue,fr,rr);   
return data;  
}

void printQueue(char *queue, int *fr, int *rr){ // 큐에 들어 있는 데이타를 모두 출력  
  
int i = *fr;  
  
if(*fr == *rr){  
printf("queue is empty!\n");  
return;  
}else{  
printf("queue = ");  
}  
  
while(*rr != i){  
printf("[%c] ", queue[i]);  
i = modAdd(i);  
}  
printf("\n");  
}  

