---
title: "Android Studio 과거 개발 환경으로 세팅하기"
date: 2020-11-23 02:00:45 +0900
categories: ["프로그래밍", "Android"]
tags: ["android studio", "gradle", "과거 버전 사용", "빌드 세팅"]
---

Android Studio 4.1.1 기준 Minimum SDK를 16미만으로 선택할 수 없었다.

구글에서 하위 SDK 버전 사용을 줄이는 정책일 것 같다.

안드로이드 개발 환경을 과거 개발 환경으로 세팅하는 과정의 시행착오를 공유하고자 한다.

![](/assets/img/posts/img_94_01.png)Android Studio - Create New Project

일단 프로젝트를 만들고, File > Project Structure 에서 Gradle Plugin과 Gradle Version을 수정할 수 있다. 

콤보박스를 누르면 보이는 선택의 폭이 적을 수 있지만, _**무시하고 직접 원하는 버전으로 타이핑**_ 해도 된다. 

![](/assets/img/posts/img_94_02.png)Android Studio - Project Structure

위 화면에서 OK를 누르면, 자동으로 프로젝트 환경 세팅이 바뀐다.

(File > Sync Project with Gradle Files 를 눌러서 직접 적용해도 된다.)

위 기입한 정보는 프로젝트에서 아래 build.gradle과 gradle-wrapper.properties에 기록된다.

![](/assets/img/posts/img_94_03.png)build.gradle ![](/assets/img/posts/img_94_04.png)gradle-wrapper.properties

원하는 compileSdkVersion, minSdkVersion, targetSdkVersion, buildToolsVersion으로 바꾸어준다.

![](/assets/img/posts/img_94_05.png)

buildToolsVersion의 경우 자동으로 다운받지만 다운이 안되는 경우, Tools > SDK Manager > Android SDK > (상단) SDK Tools 탭 > 오른쪽 하단 > Show Package Details 에 체크 표시 > 원하는 buildToolsVersion을 선택가능하다.

![](/assets/img/posts/img_94_06.png)

대부분 자동으로 바뀌었지만, 수기로 바꿔줘야 하는 부분도 있다.

1) activity_main.xml는 기본으로 세팅되는 태그가 <androidx.~ 로 시작한다. 예전 방식의 레이아웃으로 바꿔준다. 

![](/assets/img/posts/img_94_07.png)(수정전) activity_main.xml ![](/assets/img/posts/img_94_08.png)(수정후) activity_main.xml

2) build.gradle 에서 최신 문법을 사용하고 있어 오류가 발생한다.
    
    
    ```html
    Build file 'C:\Users\yorsi\AndroidStudioProjects\CatchCall\app\build.gradle' line: 33
    
    A problem occurred evaluating project ':app'.
    > Could not find method implementation() for arguments [androidx.appcompat:appcompat:1.1.0] on object of type org.gradle.api.internal.artifacts.dsl.dependencies.DefaultDependencyHandler.
    
    ```
    

아래와 같이 바꿔준다.
    
    
    ```css
        compile 'com.android.support:support-v4:25.+'
        compile 'com.android.support:appcompat-v7:25.+'
        compile 'com.android.support:design:25.+'
    ```
    

![](/assets/img/posts/img_94_09.png)

3) 내 경우에는 @style/Theme.CatchCall를 참조하고 있어서 오류가 발생했다.
    
    
    ```html
    Execution failed for task ':app:processDebugResources'.
    > com.android.ide.common.process.ProcessException: Failed to execute aapt
    ```
    

아래 불필요한 파일을 삭제해주고,

![](/assets/img/posts/img_94_10.png)themes.xml

AndroidManifest.xml 파일도 수정해준다.

![](/assets/img/posts/img_94_11.png)(수정전) AndroidManifest.xml

![](/assets/img/posts/img_94_12.png)(수정후) AndroidManifest.xml

androidx 관련 라이브러리를 삭제하고, android.support 라이브러리를 추가한다.

![](/assets/img/posts/img_94_13.png)(수정전) MainActivity.java ![](/assets/img/posts/img_94_14.png)(수정후) MainActivity.java

MainActivity.java가 Activity가 아닌 AppCompatActivity를 상속해야 한다면, AndroidManifest.xml에 @style/AppTheme가 필요하므로 아래 2가지 파일이 필요할 수 있다.

color.xml
    
    
    ```html
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <color name="colorPrimary">#008577</color>
        <color name="colorPrimaryDark">#00574B</color>
        <color name="colorAccent">#D81B60</color>
    </resources>
    ```
    

style.xml
    
    
    ```html
    <resources>
    
        <!-- Base application theme. -->
        <style name="AppTheme" parent="Theme.AppCompat.Light.DarkActionBar">
            <!-- Customize your theme here. -->
            <item name="colorPrimary">@color/colorPrimary</item>
            <item name="colorPrimaryDark">@color/colorPrimaryDark</item>
            <item name="colorAccent">@color/colorAccent</item>
        </style>
    
    </resources>
    ```
    
