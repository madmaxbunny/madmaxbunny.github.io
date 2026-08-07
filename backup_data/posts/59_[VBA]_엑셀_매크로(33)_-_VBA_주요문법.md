---
title: "[VBA] 엑셀 매크로(3/3) - VBA 주요문법"
date: "2014-01-03T10:17:27+09:00"
category: "프로그래밍/VBA"
tags: []
original_url: "https://priv.tistory.com/59"
tistory_id: 59
---

**1\. IF 문**

If i = 1Then  
  
End If  
---  
  
  * 같지 않다 : <>
  * 논리연산 : Or, And



  


**2\. IF-ELSE문**

If i = 1Then ElseIf i=2 Then 'ElseIf 띄어쓰기 안함 End IF  
---  
  


**3\. For문**

For i = 1 To 5 Next  
---  
  


**4\. Select(Switch)문**

Select Case 변수  
Case 1 ':' 안써도 됨 ' 명령1  
Case 2 ' 명령2  
End Select  
---  
  


**5\. Return;**

Private Sub CommandButton1_Click() End Sub  
---  
  
  


**6\. Break**

For i = 2 To 5   
If i = 3 Then  
End If  
Next  
---  
  
  


> [_[VBA] 엑셀 매크로(1/3) - 시작하기_](http://priv.tistory.com/57)  
> [_[VBA] 엑셀 매크로(2/3) - 엑셀 제어하기_](http://priv.tistory.com/58)
