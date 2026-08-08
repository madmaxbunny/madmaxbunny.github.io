---
title: 람다식(Lambda Expression)
date: 2015-11-20 12:10:17 +0900
categories:
- 프로그래밍
- JAVA
tags: []
---

> **[핵심 요약]**
> 람다식(Lambda Expression) 작업에 대해 실무에서 검증된 핵심 설정 및 처리 방법을 정돈해둔 노트이에요.

---

## 1. 개요 및 배경

람다식(Lambda Expression)에 관해 개발 및 인프라 운용 과정에서 접했던 내용들을 공유해볼게요.

---

## 2. 핵심 설명 및 설정 가이드

---

## 1. 개요 및 배경

---

## 2. 핵심 설명 및 설정 가이드

>  **TL;DR (핵심 요약)**  
> 람다식(Lambda Expression)에 대한 상세 설명 및 핵심 가이드이에요.

---

## 1. 개요 및 배경

람다식(Lambda Expression) 가이드 및 실무 적용 설명이에요.

---

## 2. 핵심 설명 및 설정 가이드

1\. 람다식(Lambda Expression)

[의미] 식별자 없이 실행 가능한 함수 표현식 (자바 8부터 지원)

[장점]

1) 코드가 매우 간결해진다.

2) 컬랙션 요소(대용량 데이터)를 필터링 또는 맵핑해서 쉽게 집계할 수 있다.

기존 제네릭 사용 예

```
new Thread(new Runnable() {
@Override
public void run() {
System.out.println("Hello World.");
}
}).start();

```

```
new Thread(()->{
System.out.println("Hello World.");
}).start();

```

2\. 람다식 기본 문법

람다식의 구성

(Long val1, String val2) -> { val1 + val2.length(); }

1) int 매개 변수 a의 값을 콘솔에 출력하기 위해 다음과 람다식을 작성할 수 있다.

(int a) -> {System.out.println(a); }

2) 매게 변수 타입은 런타임 시에 대입되는 값에 따라 자동인식 가능하다.

(a) -> {System.out.println(a); }

3) 하나의 매개변수만 있다면 괄호 생략, 하나의 실행문만 있다면 중괄호 생략 가능하다.

a -> System.out.println(a);

4) 매개 변수가 없다면 빈 괄호를 반드시 사용해야 한다.

()-> System.out.println(a);

5) 중괄호를 실행하고 결과값을 리턴해야 한다면 다음과 같이 사용 가능하다.

(x, y) -> { return x + y; }

6) 중괄호에 return문만 있을 경우

(x, y) -> { x + y }

3\. 타겟 타입과 함수적 인터페이스

* 람다식은 인터페이스 변수에 대입된다. 인터페이스는 직접 객체화할 수 없기 때문에 구현 클래스가 필요한데, 람다식은 익명 구현 클래스를 생성하고 객체화한다. 람다식은 대입될 인터페이스의 종류에 따라 작성 방법이 달라 지기 때문에 람다식이 대입될 인터페이스를 _타겟타입(target type)_ 이라고 한다.

*** 함수적 인터페이스**

[의미] 하나의 추상 메소드가 선언된 인터페이스

함수적 인터페이스를 작성할 때 두 개 이상의 추상 메소드가 선언되지 않도록 컴파일러가 체킹해

주는 기능이 있는데, 인터페이스 선언 시 @FunctionInterface 어노테티션을 붙이면 된다.

```

@FunctionInterface 어노테티션
public interface MyfunctionlInterface{
public void method();
public void otherMethod(); // 컴파일 오류
}

```

이 인터페이스를 타겟 타입으로 갖는 람다식은 다음과 같은 형태로 작성 가능하다.

1) 매개변수와 리턴값이 없는 람다식 : MyfunctionlInterface fi = () -> { 실행코드; }

fi.method();

2) 매개변수가 있는 람다식 : MyfunctionlInterface fi = (x) -> { 실행코드; }

fi.method(5);

3) 리턴값이 있는 람다식 : MyfunctionlInterface fi = (x, y) -> { return 값; }

int result = fi.method(2, 5);

4\. 표준 API의 함수적 인터페이스

*자바8부터 java.util.function 표준 API 패키지로 제공

종류 매개값 리턴값 비고

Consumer 있음 없음

public interface Consumer<T>{

void accept(T t);

}

Supplier 없음 있음

public interface Supplier<T>{

T get();

}

Function 있음 있음

public interface Function<T, R>{

R apply(T t);

}

// 매개값을 리턴값으로 매핑(타입변환)

Operator 있음 있음

public interface IntBinaryOperator{

applyAsInt(int, int);

}

// 매개값을 연산하고 결과를 리턴

Predicate 있음 true/fase

public interface Predicate<T>{

boolean test(T t);

}

// 리턴 타입 boolean

※ 신용권, ‘ 이것이 자바다. Java 프로그래밍 정복’, 2015, p.678-716 참조

---

## 3. 정리하며

- 본 포스트는 실무 개발 및 인프라 운용 중 검증된 노하우를 바탕으로 정리되었습니다.
- 추가 문의나 개선사항은 포스트 하단 댓글 또는 GitHub 이슈로 전달해 주세요.

---

## 3. 정리하며

관련 내용에 대해 궁금한 점이 있으시다면 언제든 편하게 질문해주세요.

---

## 3. 정리하며

관련해서 궁금하신 점이나 나눠보고 싶은 의견이 있으시다면 언제든 댓글로 편하게 말씀해주세요.
