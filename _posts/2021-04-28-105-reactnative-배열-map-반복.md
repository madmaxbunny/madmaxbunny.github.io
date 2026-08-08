---
title: "[ReactNative] 배열 Map 반복"
date: 2021-04-28 23:52:23 +0900
categories: ["기타"]
tags: []
---

> 💡 **TL;DR (핵심 요약)**  
> [ReactNative] 배열 Map 반복에 대한 상세 설명 및 핵심 가이드입니다.

---

## 1. 개요 및 배경

[ReactNative] 배열 Map 반복 가이드 및 실무 적용 설명입니다.

---

## 2. 핵심 설정 및 실행 가이드

```javascript
    // 정의
    this.state = {
    	items : []
    };
    
    // 변환
    res.data.map((obj) => {
    	var temp = {
    		label : obj.displayName,
    		value : obj.code
    	}
    
    	this.setState({
    		items : this.state.items.concat(temp)
    	});
    });
    
    // 구현
    render(){ 
    	return (
    		items = {this.state.items}
            ...
    
    ```

---

## 3. 요약 및 참고사항

- 본 포스트는 실무 개발 및 인프라 운용 중 검증된 노하우를 바탕으로 정리되었습니다.
- 추가 문의나 개선사항은 포스트 하단 댓글 또는 GitHub 이슈로 전달해 주세요.
