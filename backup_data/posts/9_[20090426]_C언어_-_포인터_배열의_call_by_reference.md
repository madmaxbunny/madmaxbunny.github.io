---
title: "[2009/04/26] C언어 - 포인터 배열의 call by reference"
date: "2009-04-26T23:33:33+09:00"
category: "프로그래밍/C/C++"
tags: ["포인터배열"]
original_url: "https://priv.tistory.com/9"
tistory_id: 9
---

포인터 배열의 내용을 

함수를 통해 바꿀수 있도록 만든 예제 입니다.

포인터의 내용을 함수로 넘겨줄때 함수 선언부와 리턴에 무엇이라 선언을 할찌 고민을 했는데.. 

아래와 같더군요.. 

공부하는데 참고하시길 바랍니다.  
  
#include <stdio.h>  
int* fun(int**,int*);

void main(){  
  
int *c, *arr[5];  
int a=1, i = 0, node[5] = {2,3,4,5,6};  
printf("Name\tAddress\t\tValue\n");  
printf("a : \t%d, \t[%d] \n\n",&a, a);

for(i=0;i<5;i++){  
arr[i] = &node[i];  
printf("nArr : \t%d, \t[%d]\n",&node[i],node[i]);  
}

printf("\n");  
for(i=0;i<5;i++){  
arr[i] = &node[i];  
printf("arr : \t%d, \t%d, \t[%d]\n",&arr[i],arr[i],*arr[i]);  
}  
  
printf("\n");  
c=fun(arr,&a);  
  
for(i=0;i<5;i++){  
printf("arr : \t%d, \t%d, \t[%d]\n",&arr[i],arr[i],*arr[i]);  
}  
printf("\n\t%d, \t[%d]\n",c,*c);  
}

int* fun(int **arr, int *a){  
arr[3] = a;   
return arr[3];  
}  
  


![](../images/img_9_01.png)
