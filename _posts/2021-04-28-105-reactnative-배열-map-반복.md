---
title: '[ReactNative] 배열 Map 반복'
date: 2021-04-28 23:52:23 +0900
categories:
- 카테고리 없음
tags: []
---
> **[핵심 요약]**
> React Native에서 배열 데이터(Array)를 map() 함수로 순회하여 리스트 컴포넌트로 렌더링하는 법입니다.

---

## 1. 개요 및 배경

[ReactNative] 배열 Map 반복은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

## 2. 핵심 설명 및 코드

> [ReactNative] 배열 Map 반복의 기본 개념과 실무 적용 명령어를 

---

[ReactNative] 배열 Map 반복은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

> [ReactNative] 배열 Map 반복 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트입니다.

---

[ReactNative] 배열 Map 반복과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유합니다.

---

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

---

이상으로 [ReactNative] 배열 Map 반복의 기초 개념과 실행 방법에 대한 공유를 마칩니다.

---

## 3. 정리하며

이상으로 [ReactNative] 배열 Map 반복의 기초 개념과 실행 방법에 대한 공유를 마칩니다.