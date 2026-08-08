---
title: '[ReactNative] code push - Android'
date: 2021-04-16 00:49:48 +0900
categories:
- 프로그래밍
- 기타
tags:
- code push
- react-native
---

> **[핵심 요약]**
> [ReactNative] code push - Android 작업에 대해 실무에서 검증된 핵심 설정 및 처리 방법을 정돈해둔 노트이에요.

---

## 1. 개요 및 배경

[ReactNative] code push - Android에 관해 개발 및 인프라 운용 과정에서 접했던 내용들을 공유해볼게요.

---

## 2. 핵심 설명 및 설정 가이드

---

## 1. 개요 및 배경

---

## 2. 핵심 설명 및 설정 가이드

>  **TL;DR (핵심 요약)**  
> [ReactNative] code push - Android에 대한 상세 설명 및 핵심 가이드이에요.

---

## 1. 개요 및 배경

[ReactNative] code push - Android 가이드 및 실무 적용 설명이에요.

---

## 2. 핵심 설명 및 설정 가이드

MS에서 제공하는 리엑트 네이티브 앱 컨텐츠 배포 서비스.

버전이 자주 바뀌기 때문에 인터넷 블로그 마다 내용이 조금씩 다르다. 어설프게 따라하다 더 고생한다. 꼭 공식 홈페이지 튜토리얼부터 확인 할 것!

### 1\. Appcenter에 앱 등록

<https://appcenter.ms> 사이트에 수기로 입력하는 방법도 있지만, 아래 코드를 콘솔에 입력하면 사이트에 자동으로 등록된다.

> sudo npm install -g code-push-cli  
> code-push register  
> Enter your token from the browser: (웹 사이트로 이동이 될텐데, 화면에 나오는 키를 console 에 입력하면 된다.)

> code-push app add 앱이름 android react-native

> code-push app add 앱이름 ios react-native

위 명령어 중 하나 실행 시, 디바이스에 해당하는 Deployment Key가 화면에 출력된다. (<https://appcenter.ms> 에서도 조회 가능하다.)

┌────────────┬───────────────────────────────────────┐  
│ Name │ Deployment Key │  
├────────────┼───────────────────────────────────────┤  
│ Production │ IB6_mqFmvTaD_kIPJCkVKo5XZ47uj │  
├────────────┼───────────────────────────────────────┤  
│ Staging │ h7shAt40KtEAz735ny9frIbsuRtg │  
└────────────┴───────────────────────────────────────┘

### 2\. Appcenter SDK를 앱 내부에 삽입

1) 프로젝트 폴더에서 아래 명령어 실행한다.

```java
npm install appcenter appcenter-analytics appcenter-crashes --save-exact
```

2) android/app/src/main/assets 경로에 appcenter-config.json 만들고 app_secret 삽입 (<https://appcenter.ms> 에서 1 단계에 등록한 앱을 클릭하면 조회 가능)

```html
{
"app_secret": "{APP_SECRET_VALUE}"
}
```

3) res/values/strings.xml 에 아래 2줄을 추가한다.

```html
<string name="appCenterCrashes_whenToSendCrashes" moduleConfig="true" translatable="false">DO_NOT_ASK_JAVASCRIPT</string>
<string name="appCenterAnalytics_whenToEnableAnalytics" moduleConfig="true" translatable="false">ALWAYS_SEND</string>
```

※ 참조

[docs.microsoft.com/en-us/appcenter/sdk/getting-started/react-native#312-integrate-react-native-android](https://docs.microsoft.com/en-us/appcenter/sdk/getting-started/react-native#312-integrate-react-native-android)

[ Get Started with React Native - Visual Studio App Center Get Started with React Native docs.microsoft.com ](https://docs.microsoft.com/en-us/appcenter/sdk/getting-started/react-native#312-integrate-react-native-android)

### 3\. 배포 준비

1) appcenter-cli 설치

```html
npm install -g appcenter-cli
```

2) android/settings.gradle 하단에 아래 정보 삽입

```java
// include ':app'
include ':app', ':react-native-code-push'
project(':react-native-code-push').projectDir = new File(rootProject.projectDir, '../node_modules/react-native-code-push/android/app')

```

3) android/app/build.gradle 하단에 아래 정보 삽입

```java
...
// apply from: "../../node_modules/react-native/react.gradle"
apply from: "../../node_modules/react-native-code-push/android/codepush.gradle"
...
```

앱 빌드 시 아래 오류 발생하면, 위 첫 줄은 주석 처리한다.

```java
FAILURE: Build failed with an exception.

* Where:
Script '/Users/khlim/Dev/react-native/codePushApp/node_modules/react-native/react.gradle' line: 132

* What went wrong:
A problem occurred configuring project ':app'.
> Cannot add task 'bundleDebugJsAndAssets' as a task with that name already exists.
```

4) MainApplication.java 파일 에 getJSBundleFile 함수 오버라이딩

```java
...
// 1. Import the plugin class.
import com.microsoft.codepush.react.CodePush;
public class MainApplication extends Application implements ReactApplication {
private final ReactNativeHost mReactNativeHost = new ReactNativeHost(this) {
    ...

    @Override
    protected String getJSBundleFile() {
        return CodePush.getJSBundleFile();
    }
};
}
```

5) android/app/src/main/res/values/strings.xml 파일에 1. 단계에서 획득한 Deployment Key 추가

```html
<string moduleConfig="true" name="CodePushDeploymentKey">{Deployment Key}</string>
```

**6) App.js 파일에 아래 코드 추가**

```javascript
import codePush from 'react-native-code-push';

const codePushOptions = {
checkFrequency: codePush.CheckFrequency.ON_APP_RESUME
}
export default codePush(codePushOptions)(App)
```

※ 블로그마다 js 코드 부분이 생략된 경우가 많았는데, 필자의 경우 js 코드가 입력되지 않으면

appcenter codepush 명령을 실행 시, <https://appcenter.ms>에 코드가 업로드만 되었고 실제 앱에는 변화가 없었다.

(하단 오른쪽에 ACTIVE 영역에 0로 나오고 앱에 변화는 없는 상태)

![](/assets/img/posts/img_102_01.png)

[docs.microsoft.com/en-us/appcenter/distribution/codepush/rn-get-started#plugin-installation-and-configuration-for-react-native-060-version-and-above-android](https://docs.microsoft.com/en-us/appcenter/distribution/codepush/rn-get-started#plugin-installation-and-configuration-for-react-native-060-version-and-above-android)

[ Get Started with the React Native Client SDK - Visual Studio App Center Getting started with the React Native SDK & CodePush docs.microsoft.com ](https://docs.microsoft.com/en-us/appcenter/distribution/codepush/rn-get-started#plugin-installation-and-configuration-for-react-native-060-version-and-above-android)

### 4\. 배포

1) 프로젝트 폴더에서 아래 명령어 설치 및 실행

```html
npm install --save react-native-code-push

appcenter codepush release-react -a khlim/codePushTestApp -d Production
appcenter codepush release-react -a khlim/codePushTestApp -d Staging
```

앱 종료 후 다시 실행해야 변화가 있었다. 

### 5\. 예외 케이스

```html
The uploaded package was not released because it is identical to the contents of the specified deployment's current release.
```

> 변경된 부분이 없으면 발생한다.

```html
our target-binary-version "1.0" will be treated as "1.0.X".

Error: {"message":"Failed to initialize file upload process."}
```

> npm start로 동작시킨 서버가 종료되면 발생. 다시 실행하면 된다.

### 6\. 기타

Multi-Deployment Testing

[docs.microsoft.com/en-us/appcenter/distribution/codepush/rn-deployment](https://docs.microsoft.com/en-us/appcenter/distribution/codepush/rn-deployment)

[ Using the React Native SDK with CodePush – Distribution - Visual Studio App Center Distribution with React Native SDK and CodePush docs.microsoft.com ](https://docs.microsoft.com/en-us/appcenter/distribution/codepush/rn-deployment)

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
