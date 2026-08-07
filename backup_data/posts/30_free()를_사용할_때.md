---
title: "free()를 사용할 때"
date: "2010-01-09T16:09:11+09:00"
category: "프로그래밍/C/C++"
tags: []
original_url: "https://priv.tistory.com/30"
tistory_id: 30
---

  
void deleteNode(NODE* hd, int delCnt){  
  
int i;  
NODE* delPt;

for(i=1;i<delCnt;i++){ // delCnt만큼 노드순회후 삭제  
hd = hd->next;  
}  
delPt = hd->next;  
hd->next = hd->next->next;  
  
free(delPt);  
}  
//////////////////////////////////////////////////////////////////////////

void deleteNode(NODE* hd, int delCnt){  
  
int i;  
NODE* delPt;

for(i=1;i<delCnt;i++){ // delCnt만큼 노드순회후 삭제  
hd = hd->next;  
}  
hd->next = hd->next->next;  
free(hd->next);  
}  
//////////////////////////////////////////////////////////////////////////  
아래와 같이 하면 애러난다
