---
title: "React-native 개발 환경 설정"
date: 2021-02-09 23:51:53 +0900
categories: ["프로그래밍"]
tags: []
---

> **[핵심 요약]**
> React-native 개발 환경 설정 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트이에요.

---

## 1. 개요 및 배경

React-native 개발 환경 설정과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유해요.

---

## 2. 핵심 설명 및 코드

## **1\. Mac**

### 1\. 개발 환경 설정

<https://gist.github.com/falsy/8aa42ae311a9adb50e2ca7d8702c9af1>
    
    
```java
NVM 설치
$ sudo curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash
$ nvm --version
0.33.11

노드 설치
$ nvm install 6.10.1
$ nvm ls
$ use X.X.X (node 버전정보)
$ node -v 
v10.15.1
$ npm --version	(npm 자동 설치됨)
6.4.1

$ sudo gem install cocoapods -v 1.8.4
$ pod --version
1.8.4

$ npm install -g react-native-cli
$ react-native -vsersion  
react-native-cli: 2.0.1
react-native: n/a

$ java -version
java version "1.8.0_221"
Java(TM) SE Runtime Environment (build 1.8.0_221-b11)
Java HotSpot(TM) 64-Bit Server VM (build 25.221-b11, mixed mode)

```
    

  * Xcode > Preperences > Locations > Command Line Tools : Xcode 11.3.1 선택
  * AndroidStudio >

![](/assets/img/posts/img_96_01.png)
    
    
```html
$ vi ./.zshrc
export ANDROID_HOME=/Users/khlim/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools

export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_221.jdk/Contents/Home

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" # This loads nvm
```
    

### 2\. 프로젝트 생성
    
    
```java
$ react-native init --version 0.61.5 프로젝트명
$ react-native -version  
react-native-cli: 2.0.1
react-native: 0.61.5

```
    

### 3\. 실행
    
    
```html
$ cd 프로젝트명
$ cd npm start

신규 터미널을 열고 해당 프로젝트 폴더 안에서
$ react-native run-android
$ react-native run-ios

```
    

### 4\. 오류 

#### case 1.
    
    
```java
error Failed to install the app. Make sure you have the Android development environment set up: https://facebook.github.io/react-native/docs/getting-started.html#android-development-environment. Run CLI with --verbose flag for more details.
Error: Command failed: ./gradlew app:installDebug -PreactNativeDevServerPort=8081
```
    

해결 방법) cd android && chmod +x gradlew

<https://stackoverflow.com/questions/56891033/facing-issue-failed-to-install-the-app-make-sure-you-have-the-android-develop>

#### case 2.
    
    
```java
xecution failed for task ':app:compileDebugJavaWithJavac'.
> Could not find tools.jar.
```
    

해결 방법) JAVA가 설치되어 있더라도 JAVA_HOME을 환경 변수로 등록해야함

#### case 3.
    
    
```java
안드로이드 애뮬레이터 실행 시 오류 발생
```
    

해결 방법) Android 버전을 29 -> 23으로 낮추니깐 잘됨. 28이상부터 이슈 있음

case 4.

2021.04.10 

Node LTE 버전 14.16.1로 업데이트

> react-native run-ios 실행 시 아래 오류 발생
    
    
```java
error Could not find "Podfile.lock" at /Users/khlim/Dev/react-native/secondApp/ios/Podfile.lock. Did you run "pod install" in iOS directory?
info Found Xcode project "secondApp.xcodeproj"
info Launching iPhone 12 (iOS 14.4)
info Building (using "xcodebuild -project secondApp.xcodeproj -configuration Debug -scheme secondApp -destination id=32E15FB9-85B6-469A-A374-8925A968C23F")
error Failed to build iOS project. We ran "xcodebuild" command but it exited with error code 65. To debug build logs further, consider building your app with Xcode.app, by opening secondApp.xcodeproj.
Command line invocation:
    /Applications/Xcode.app/Contents/Developer/usr/bin/xcodebuild -project secondApp.xcodeproj -configuration Debug -scheme secondApp -destination id=32E15FB9-85B6-469A-A374-8925A968C23F
```
    

iOS 폴더에서 아래 명령어 실행

> cd ios   
> pod repo update  
> pod install
    
    
```java
Updating spec repo `trunk`

CocoaPods 1.10.1 is available.
To update use: `sudo gem install cocoapods`

For more information, see https://blog.cocoapods.org and the CHANGELOG for this version at https://github.com/CocoaPods/CocoaPods/releases/tag/1.10.1

khlim@khlimui-MacBookPro ios % pod install
Analyzing dependencies
Fetching podspec for `DoubleConversion` from `../node_modules/react-native/third-party-podspecs/DoubleConversion.podspec`
Fetching podspec for `RCT-Folly` from `../node_modules/react-native/third-party-podspecs/RCT-Folly.podspec`
Fetching podspec for `glog` from `../node_modules/react-native/third-party-podspecs/glog.podspec`
[!] `OpenSSL-Universal` requires CocoaPods version `>= 1.9`, which is not satisfied by your current version, `1.8.4`.
```
    

> sudo gem install cocoapods  
> pod repo update  
> pod install

이후에 다시 react-native run-ios 실행하니 정살 실행됨

case 5.

> nvm install 14.16.2

신규 노드를 설치하게되면 해당 노드위에 리엑트 네이티브를 다시 설치해줘야 함. 버전별 독립된 영역인 듯..

case 6.

code 명령어 사용하기 위해 ~/.zshrc 파일에 vscode path를 추가해줘야 한다. 띄어쓰기 있어서 ""으로 감싸줘야 함
    
    
```html
export VSCODE_HOME="/Applications/Visual Studio Code.app/Contents/Resources/app/bin"
export PATH=$PATH:$VSCODE_HOME
```
    

case 7.
    
    
```html
npm start

> codePushApp@0.0.1 start /Users/autoever/Dev/react-native/codePushApp
> react-native start

/Users/autoever/Dev/react-native/codePushApp/node_modules/react-native/node_modules/@react-native-community/cli/build/index.js:178
  const cmd = _commander().default.command(command.name).action(async function handleAction(...args) {
                                                                ^^^^^
SyntaxError: missing ) after argument list
    at createScript (vm.js:56:10)
    at Object.runInThisContext (vm.js:97:10)
    at Module._compile (module.js:542:28)
    at Object.Module._extensions..js (module.js:579:10)
    at Module.load (module.js:487:32)
    at tryModuleLoad (module.js:446:12)
    at Function.Module._load (module.js:438:3)
    at Module.require (module.js:497:17)
    at require (internal/module.js:20:19)
    at Object.<anonymous> (/Users/autoever/Dev/react-native/codePushApp/node_modules/react-native/cli.js:13:11)

npm ERR! Darwin 20.2.0
npm ERR! argv "/Users/autoever/.nvm/versions/node/v6.10.1/bin/node" "/Users/autoever/.nvm/versions/node/v6.10.1/bin/npm" "start"
npm ERR! node v6.10.1
npm ERR! npm  v3.10.10
npm ERR! code ELIFECYCLE
npm ERR! codePushApp@0.0.1 start: `react-native start`
npm ERR! Exit status 1
npm ERR! 
npm ERR! Failed at the codePushApp@0.0.1 start script 'react-native start'.
npm ERR! Make sure you have the latest version of node.js and npm installed.
npm ERR! If you do, this is most likely a problem with the codePushApp package,
npm ERR! not with npm itself.
npm ERR! Tell the author that this fails on your system:
npm ERR!     react-native start
npm ERR! You can get information on how to open an issue for this project with:
npm ERR!     npm bugs codePushApp
npm ERR! Or if that isn't available, you can get their info via:
npm ERR!     npm owner ls codePushApp
npm ERR! There is likely additional logging output above.

npm ERR! Please include the following file with any support request:
npm ERR!     /Users/autoever/Dev/react-native/codePushApp/npm-debug.log
```
    

신규 노드 설치 후 nvm use 명령어를 사용했어도, vscode 터미널 상에는 다시 nvm use 를 다시 사용해야 한다.

번거롭다면 아래처럼 default 설정이 가능하다.
    
    
```html
nvm alias default 14.16.1
```
    

case 8.
    
    
```javascript
Make sure you're either running Metro (run 'react-native start') or that your bundle 'index.android.bundle' is packaged correctly for release.
```
    

해결법 1. 노드 버전을 확인한다. 

해결법 2. 아래 순서대로 실행

1) [패키지명]/android/app/src/main/assets 폴더가 있는지 확인하고 없으면 생성  
2) [패키지명]/android 폴더에서 ./gradlew clean 실행  
3) [패키지명] 폴더에서 아래 명령어 실행
    
    
```javascript
react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle --assets-dest android/app/src/main/res
```
    

4) react-native run-android

## **2\. Windows (10)**

### 1\. 개발 환경 설정
    
    
```html
NVM 설치
1. https://github.com/coreybutler/nvm-windows/releases
2. nvm-setup.zip 다운로드 및 설치
> nvm --version
Running version 1.1.7.

> nvm install 14.15.5
버전은 Nodejs 홈페이지 참조(https://nodejs.org/ko/)

> nvm use 14.15.5
> nvm ls
14.15.5

> node -v
'node'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는
배치 파일이 아닙니다.

use 키워드로 사용할 버전을 명시해야 한다.
> nvm use 14.15.5
Now using node v14.15.5 (64-bit)

> node -v 
v14.15.5

> npm --version
6.14.11

> npm install -g react-native-cli
> react-native -vsersion  
react-native-cli: 2.0.1
react-native: n/a

> java -version
openjdk version "1.8.0_265"
OpenJDK Runtime Environment (build 1.8.0_265-b01)
OpenJDK 64-Bit Server VM (build 25.265-b01, mixed mode)

```
    

  * AndroidStudio >

![](/assets/img/posts/img_96_02.png)

필자는 AMD Ryzen 5 3600 프로세서라 [Android Emulator Hypervisor Driver for AMD Processors(Installer)를 설치했다. 인터넷에 해당 옵션 사용 위해서는 [Windows 기능]에 Hyper-V, Windows 하이퍼바이저 플랫폼을 설치해야한다는 글이 있던데.. 필자는 없이 설치 가능했다. 

### 2\. 프로젝트 생성
    
    
```html
$ react-native init 프로젝트명
$ react-native -version  
react-native-cli: 2.0.1
react-native: 0.63.5

```
    

### 3\. 실행
    
    
```html
$ cd 프로젝트명
$ cd npm start

신규 터미널을 열고 해당 프로젝트 폴더 안에서
$ react-native run-android

```
    

  * 두번째 설치라 윈도우 환경에서는 버전을 명시하지 않고 설치했다. 문제 없이 동작한다.
  * VM 에서는 안드로이드 애뮬레이터를 실행할 수 없었다.
  * react-native run-android 명령을 실행하면 애뮬레이터가 스스로 켜진 후 앱이 실행된다. 

### 2\. 오류

#### case 1. PowerShell 또는 VS Code Terminal에서 명령어 실행 시 아래와 같은 매시지 발생.
    
    
```html
react-native : 이 시스템에서 스크립트를 실행할 수 없으므로 C:\Users\-\AppData\Roaming\npm\react-native.ps1 파일을
로드할 수 없습니다. 자세한 내용은 about_Execution_Policies(https://go.microsoft.com/fwlink/?LinkID=135170)를 참조하십시
오.
위치 줄:1 문자:1
+ react-native
+ ~~~~~~~~~~~~
    + CategoryInfo          : 보안 오류: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```
    

해결 방법)

  1. PowerShell 관리자권한으로 실행
  2. > Set-ExecutionPolicy RemoteSigned

![](/assets/img/posts/img_96_03.png)

설명 : 

  * (defalut) Restricted : ps1 스크립트 파일을 로드하여 실행할 수 없음
  * RemoteSigned : 신뢰된 배포자에 의해 서명된 원격 컴퓨터의 스크립트 파일 실행 가능

### case 2.
    
    
```html
BUILD FAILED in 16s

error Failed to install the app. Make sure you have the Android development environment set up: https://reactnative.dev/docs/environment-setup. Run CLI with --verbose flag for more details.
Error: Command failed: gradlew.bat app:installDebug -PreactNativeDevServerPort=8081
```
    

해결 방법) 

환경변수 추가 : %ANDROID_HOME%

PATH 추가 : %ANDROID_HOME%\tools 

## **3\. Ubuntu 20.04 (with VirtualBox)**

  * VirtualBox의 경우 Android 애뮬레이터가 동작하지 않아 실단말을 연결하여 테스트하였다.

### 1\. 개발 환경 설정
    
    
```html
NVM 설치
> curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash
https://github.com/nvm-sh/nvm 참고
> vi ~/.bash_profile
환경변수 추가
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm

> nvm --version
0.37.2

> nvm install 14.15.5
> nvm ls
14.15.5

nvm use 14.15.5 과정없이 바로 사용 가능
> node -v 
v14.15.5

> npm --version
6.14.11

> npm install -g react-native-cli
> react-native -vsersion  
react-native-cli: 2.0.1
react-native: n/a

> java -version
Openjdk version "1.8.0_282"
OpenJDK Runtime Environment (build 1.8.0_282-8u282-b08-0ubuntu1~20.04-b08)
OpenJDK 64-Bit Server VM (build 25.282-b08, mixed mode)

Android Studio 설치
> sudo snap install android-studio --classic
환경변수 추가
export ANDROID_HOME=/home/khlim/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/platform-tools (adb 사용위해 추가함)

```
    
    
    
```html
> vi ./.bash_profile
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export PATH=$PATH:$JAVA_HOME/bin

export ANDROID_HOME=/home/khlim/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/platform-tools

export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
```
    

### 

### 

### 2\. 오류

case 1. 
    
    
```html
BUILD FAILED in ~

error Failed to install the app. Please accept all necessary Android SDK licenses 
using Android SDK Manager: "$ANDROID_HOME/tools/bin/sdkmanager --licenses". 
Run CLI with --verbose flag for more details.
Error: Command failed: ./gradlew app:installDebug -PreactNativeDevServerPort=8081
```
    

해결 방법) Android SDK > SDK Tools 에서 Google Play Licensing Library 설치

case 2.
    
    
```html
BUILD FAILED in ~

error Failed to install the app. Make sure you have an Android emulator running or 
a device connected. Run CLI with --verbose flag for more details.
Error: Command failed: ./gradlew app:installDebug -PreactNativeDevServerPort=8081
Note: /home/khlim/dev/react-native/firstApp/android/app/src/debug/java/com/firstapp/ReactNativeFlipper.
java uses or overrides a deprecated API.​
```
    

디바이스 찾지 못함.

해결 방법) 

> adb devices 

> adb shell

터미널에서 위 명령어 통해 device 접속 상태 점검 후 재접속

---

## 3. 정리하며

관련해서 궁금하신 점이나 나눠보고 싶은 의견이 있다면 댓글로 편하게 말씀해주세요.
