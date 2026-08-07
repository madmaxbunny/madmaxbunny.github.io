---
title: "Binary Tree"
date: "2010-01-09T14:15:30+09:00"
category: "카테고리 없음"
tags: ["이진트리", "트리"]
original_url: "https://priv.tistory.com/14"
tistory_id: 14
---

  
#include <stdio.h>  
#include <stdlib.h>

typedef struct _NODE{  
int key;  
struct _NODE *left;  
struct _NODE *right;  
} NODE;

NODE* insertNode(NODE*,int);  
void preorder(NODE*);  
void inorder(NODE*);  
void postorder(NODE*);

void main(){

int num, i, input;  
NODE *tree = NULL;  
  
printf("입력받을 노드의 수 갯수:");  
scanf("%d",&num);  
printf("%d개의 노드의 수 입력 \n", num);  
for(i=0;i<num;i++){  
scanf("%d",&input);  
tree = insertNode(tree, input);  
}  
printf("\n\n**결과**\n");  
  
printf("\npreorder:");  
preorder(tree);  
printf("\ninorder:");  
inorder(tree);  
printf("\npostorder:");  
postorder(tree);  
printf("\n");  
  
//fflush(stdin);  
//getchar();  
}

NODE* insertNode(NODE *t, int data){

NODE *root;  
if(t==NULL){  
root = (NODE*)malloc(sizeof(NODE));  
root->left = NULL;  
root->right = NULL;  
root->key = data;  
return root;  
}

if(data < t->key){  
t->left = insertNode(t->left,data);  
return t;  
}else{  
t->right = insertNode(t->right,data);  
return t;  
}  
}

void preorder(NODE *t){

if(t!=NULL){  
printf("%d ",t->key);  
preorder(t->left);  
preorder(t->right);  
}  
}

void inorder(NODE *t){  
  
if(t!=NULL){  
inorder(t->left);  
printf("%d ",t->key);  
inorder(t->right);  
}  
}

void postorder(NODE *t){  
  
if(t!=NULL){  
postorder(t->left);  
postorder(t->right);  
printf("%d ",t->key);

}  
}
