---
title: "[정렬] Bubble sort"
date: "2010-01-09T15:57:09+09:00"
category: "카테고리 없음"
tags: ["bubble", "bubble sort", "sort"]
original_url: "https://priv.tistory.com/25"
tistory_id: 25
---

#include <stdio.h>  
#define ARRYSIZ 200

void bubbleSort(int*,int); // bubbleSort  
void prntData(int*,int); // 배열의 내용 출력

void main(){

int siz = 8, dataAry[ARRYSIZ] = {2,0,0,6,5,5,5,4}; // data배열, data의 크기  
printf("\nBefore bubble sort:\n");  
prntData(dataAry,siz); // 배열의 내용 출력  
printf("\n\n");  
bubbleSort(dataAry,siz); // bubbleSort  
printf("\nAfter bubble sort:\n");  
prntData(dataAry,siz); // 배열의 내용 출력  
}

void prntData(int* dataAry,int siz){ // 배열의 내용 출력

int i=0;  
while(i<siz){  
printf("[%d] ",dataAry[i++]);  
}  
printf("\n");  
}

void bubbleSort(int* dataAry, int siz){ // bubble sort

int i,j,temp;  
for(i=siz-1;i>=0;i--){  
for(j=0;j<i;j++){  
if(dataAry[j]>dataAry[j+1]){ //뒤에 값과 비교하여 크면  
temp = dataAry[j+1]; //값을 교환한다.  
dataAry[j+1] = dataAry[j];  
dataAry[j] = temp;  
}  
}  
prntData(dataAry,siz); // 배열의 내용 출력  
printf("\n");  
}

}
