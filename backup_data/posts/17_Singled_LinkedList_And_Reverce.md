---
title: "Singled LinkedList And Reverce"
date: "2010-01-09T14:32:36+09:00"
category: "프로그래밍/Data Structure"
tags: ["LinkedList", "Singled", "링크드리스트"]
original_url: "https://priv.tistory.com/17"
tistory_id: 17
---

#include <stdio.h>  
#include <stdlib.h>

typedef struct _NODE{  
int data; // 데이터  
struct _NODE *next; // 다음노드의 주소  
}NODE;

  
NODE* createNode(); //해드노드 만들기  
NODE* insertNode(NODE*,int); //마지막노드뒤에 새노드 삽입, 새노드 주소 리턴  
NODE* reversNode(NODE*); //반전(reverse)   
void deleteNode(NODE*,int); //해당번째의 노드를 삭제한다.   
void prntNode(NODE*); //모든노드 출력  
void endList(NODE*); //리스트 종료 모든 노드 삭제

void main(){

NODE *hd, *pt; // hd = 첫노드주소 pt = 마지막노드 주소  
  
pt = hd = createNode();  
  
pt = insertNode(pt,2);  
pt = insertNode(pt,0);  
pt = insertNode(pt,0);  
pt = insertNode(pt,6);  
pt = insertNode(pt,5);  
pt = insertNode(pt,5);  
pt = insertNode(pt,5);  
pt = insertNode(pt,4);  


printf("\n");  
prntNode(hd);  
printf("\n");  
// deleteNode(hd,4); //delete(hd,삭제노드순서)  
// prntNode(hd);

printf("\n\n<revers>\n");  
hd = reversNode(hd);  
prntNode(hd);  
printf("\n");  
  
endList(hd); //만들었던 모든 노드 삭제(free)  
}

  
NODE* createNode(){  
  
NODE *head = (NODE*)malloc(sizeof(NODE)); //리스트를 생성하기 위해 head노드 생성  
head ->data = NULL;  
head ->next = NULL;  
  
return head;  
}

NODE* insertNode(NODE* pt,int data){  
  
NODE *newNode = (NODE*)malloc(sizeof(NODE));  
pt->next = newNode; // 새노드를 마지막 노드 뒤에 삽입한다.  
newNode->next = NULL;  
newNode->data = data;  
  
return newNode; // 생선한 노드의 주소값 리턴  
}  
void deleteNode(NODE* hd, int cnt){  
  
int i;  
NODE *delPt, *temp;  
  
for(i=1;i<cnt;i++){ // cnt만큼 노드순회후 삭제  
if(NULL==hd->next){// (예외 처리)cnt만큼 노드순회후 더 이상 노드가 없을 경우  
  
printf("Not find node%d!\n",cnt);  
return;  
}  
temp = hd;   
hd = hd->next;  
}  
  
if(NULL==hd->next){  
//for문으로 cnt-1만큼 순회후 그 노드의 next를 삭제하는데  
//cnt-1과 현재 생성된 노드의 수가 일치하게 되면 next값이 null인데도 불구하고   
//아래 hd->next = hd->next->next; 구문을 실행하게 된다.   
//그래서 NULL==hd->next도 예외처리 해야한다.  
printf("Not find node%d!\n",cnt);  
return;  
}   
delPt = hd->next;  
hd->next = hd->next->next;  
  
free(delPt);  
}

void prntNode(NODE* hd){

while(NULL != hd->next){ //노드의 next가 null이 될때까지 순회   
printf("%d", hd->next->data);   
hd = hd->next;   
}

}

void endList(NODE* hd){  
  
if(NULL==hd->next){ //마지막 남은 해드노드 삭제 free();  
free(hd);  
return;  
}  
int cnt=0;  
NODE *pt;  
while(NULL != hd->next){ //노드의 next가 null이 될때까지 순회   
  
pt = hd;  
hd = hd->next; //일단 hd를 옴겨 놓고   
free(pt); //노드 삭제  
}  
}  
NODE* reversNode(NODE* hd){  
  
NODE *pt, *pt2; //리버스하기 위한 두개의 포인터노드 지정

if(NULL==hd->next) return hd; // 예외 처리(해드노드밖에 존재하지 않을경우)  
  
pt2 = hd->next->next;  
hd->next->next = NULL;  
  
while(pt2!=NULL){  
pt = hd->next;  
hd->next = pt2;  
pt2 = pt2 ->next;  
hd->next->next = pt;  
}  
  
return hd;  
}  

