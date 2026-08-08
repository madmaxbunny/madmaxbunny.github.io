---
title: "Tree ( levelOrder, printTree )"
date: 2010-01-09 15:47:34 +0900
categories: ["프로그래밍", "Data Structure"]
tags: []
---

> **[핵심 요약]**
> Tree ( levelOrder, printTree ) 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트입니다.

---

## 1. 개요 및 배경

Tree ( levelOrder, printTree )과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유합니다.

---

## 2. 핵심 설명 및 코드

```
  
#include 
#include 
#include 

#define QUESIZ 90000                                                        // QUESIZ

typedef struct _NODE{
        int key;
        struct _NODE *left;
        struct _NODE *right;
} NODE;

//주요기능
NODE* makeRendTree(NODE*,int,int*);                //입력받은 수만큼의 노드를 가진 랜덤 트리를 만들어준다. 
NODE* findNode(NODE*,int);                                //값은 key값을 찾아 주소를 return
NODE* findPrntNode(NODE*,int);                        //찾는 노드의  부모노드의 주소를 return  
NODE* selectChild(NODE*,int);                        //부모주소의 주소를 입력받아 자식 노드주소 return
NODE* insertNode(NODE*,int,int*);                //트리에 노드 삽입
void deleteNode(NODE*,int,int*);                //입력한 key값을 삭제한다.
void searchDelNode(NODE*,int,int*);                //입력한 key값을 트리에서 찾아서 삭제한다.
int deepFind(NODE*,int);                                //트리의 deep을 return

//순회
void preorder(NODE*);                                        //전위순회
void inorder(NODE*);                                        //중위순회
void postorder(NODE*);                                        //후위순회
void levelorder(NODE*);                                        //래밸순회

//트리출력 
void pntTreeNode(NODE*,int,int);                //트리출력(노드간 여백없음)
void pntTreeNodeSpce(NODE*,int,int);        //트리출력(노드간 여백있음)

// Queue 관련
void enqueue(NODE**,int*,int*,NODE*);        //input
NODE* dequeue(NODE**,int*,int*);                //output
int modAdd(int);                                                //원형큐이므로 모드연산 함수

//////////////////////////        
void main(){
        
        int num=3, i, input, cnt=0, deep = 0;                // cnt = 노드의 수 
        NODE *tget, *root = NULL;

        root = makeRendTree(root,10,&cnt);        //랜덤 트리 생성 (root,노드수)

        printf("입력받을 노드의 개수:");
        //scanf("%d",&num);
        printf("%d개의 노드의 수 입력 \n", num);
        for(i=0;i\n");
        //pntTreeNode(root,cnt,deep);
        pntTreeNodeSpce(root,cnt,deep);

        //finding
        printf("\n\n");
        tget = findNode(root,200);
        printf("\n",tget->key, tget);
        
        //delete Node 200
        printf("\n\n");
        searchDelNode(root,200,&cnt);                        //트리에서 key 200의 노드를 제거
                
        //tree 만들기
        //pntTreeNode(root,cnt,deep);
        printf("\n");
        pntTreeNodeSpce(root,cnt,deep);

        //orders
        printf("\n\n[levelOrder]:");
        levelorder(root);
        printf("\n[preorder]:");
        preorder(root);
        printf("\n[inorder]:");
        inorder(root);
        printf("\n[postorder]:");
        postorder(root);
        printf("\n");
}

void searchDelNode(NODE *root, int key, int *cnt){        //트리에서 노드를 찾아 삭제
        NODE *parents;
        //NODE *child; 
        parents = findPrntNode(root,key);        //입력한 KEY값에 대한 부모노드의 주소를 리턴한다.
        //printf("\n",parents->key, parents);
        //child = selectChild(parents,200);
        //if(!child) printf("error!");
        //printf("\n",child->key, child);
        deleteNode(parents,key,cnt);
        
 }

NODE* selectChild(NODE* parents, int key){

        //만약 왼쪽과 오른쪽 노드의 key가 같다면 왼쪽노드가 우선시 된다.
        if(parents->left){        // prnt에 왼쪽 자식 노드가 있다면
                if(key==parents->left->key) return parents->left ;        // 자식노드의 key와 일치하는지 확인
        }
        
        if(parents->right){        // prnt에 오른쪽 자식 노드가 있다면
                if(key==parents->right->key) return parents->right ;        // 자식노드의 key와 일치하는지 확인
        }
                
        return NULL;
}

void deleteNode(NODE *parents, int key, int *cnt){

        NODE *ptr;                                                                        //자신의 주소
        ptr = selectChild(parents, key);
        if(NULL==ptr->left && NULL==ptr->right){        //leaf노드라면
                if(parents->left == ptr){
                        parents->left = NULL;
                }else{
                        parents->right = NULL;
                }
                free(ptr);
                (*cnt)--;
                return;
        }else if(!(parents->left)){        //왼쪽 자식이 NULL이면(오른쪽 자식만 가지고 있다면)
                ptr->key = ptr->right->key;
                deleteNode(parents->right,ptr->key,cnt);
        }else{                                        //두자식 또는 왼쪽 자식노드만 갖고 있다면
                ptr->key = ptr->left->key;
                deleteNode(parents->left,ptr->key,cnt);
        }
}

NODE* findPrntNode(NODE *parents, int key){
        //만약 왼쪽과 오른쪽 노드의 key가 같다면 왼쪽노드가 우선시 된다.
        if(parents->left){        // prnt에 왼쪽 자식 노드가 있다면
                if(key==parents->left->key) return parents ;        // 자식노드의 key와 일치하는지 확인
        }
        if(parents->right){        // prnt에 오른쪽 자식 노드가 있다면
                if(key==parents->right->key) return parents ;        // 자식노드의 key와 일치하는지 확인
        }

        if(key < parents->key){
                parents = findPrntNode(parents->left,key);
        }else{
                parents = findPrntNode(parents->right,key);
        }
        return parents;
}

NODE* findNode(NODE *ptr, int key){
        
        NODE *tget;
        if(key==ptr->key) return ptr;
        
        if(key < ptr->key){
                tget = findNode(ptr->left,key);
                return tget;
        }else{
                tget = findNode(ptr->right,key);
                return tget;
        }
}

NODE* makeRendTree(NODE* root, int num, int *cnt){
        
        int i;
        
        srand(time(NULL));
        for(i=0;ileft = NULL;
        emptyNd->right = NULL;
        emptyNd->key = NULL;
        
        if(!ptr) return;                                                //출력할 노드가 없다면 종료한다.
        
        enqueue(queue,&fr,&rr,ptr);        
        while(deep>=h){                                                //모든 노드를 출력하면 종료
                ptr = dequeue(queue,&fr,&rr);
                if(ptr->key) ++cnt;                                        //cnt, 현재 데이터 노드가 몇개 인지 가리킴
                ++ant;                                                                //ant, 현재 래밸의 몇번째 노드인인지 가리킴
                //printf("<%D [%x]>
```

---

## 3. 정리하며

