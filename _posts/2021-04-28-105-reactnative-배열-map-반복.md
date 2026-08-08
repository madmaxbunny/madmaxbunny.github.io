---
title: "[ReactNative] 배열 Map 반복"
date: 2021-04-28 23:52:23 +0900
categories: ["카테고리 없음"]
tags: []
---

> **[핵심 요약]**
> [ReactNative] 배열 Map 반복 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트이에요.

---

## 1. 개요 및 배경

[ReactNative] 배열 Map 반복과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유해요.

---

## 2. 핵심 설명 및 코드

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

## 3. 정리하며

관련해서 궁금하신 점이나 나눠보고 싶은 의견이 있다면 댓글로 편하게 말씀해주세요.
