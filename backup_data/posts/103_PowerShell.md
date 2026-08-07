---
title: "PowerShell"
date: "2021-04-16T17:38:24+09:00"
category: "프로그래밍"
tags: []
original_url: "https://priv.tistory.com/103"
tistory_id: 103
---

#### 파워쉘 확인
    
    
    ```javascript
    $PSVersionTable
    ```
    

#### 파일 복사
    
    
    ```javascript
    Copy-Item -Path "d:\source\sample.txt" -Destination "d:\target"
    ```
    

#### 파일 읽기/쓰기
    
    
    ```javascript
    # 읽기
    $text = Get-Content "파일경로"
    
    # 쓰기
    Set-Content "파일경로" "내용"
    ```
    

#### 보안 스트링
    
    
    ```javascript
    $secureString = Read-Host -AsSecureString
    
    # SecureString 파일로 저장하기
    Read-Host -AsSecureString | ConvertFrom-SecureString | Set-Content "파일경로\dev.key"
    ```
    

#### 원격 서버에 파일 복사

\- 젠킨스로 윈도우 서버 제어할 목적으로 작성

\- 응용하면 굳이 원격 mstsc를 사용할 필요가 없을듯

\- 반대의 경우 -FromSession 사용
    
    
    ```javascript
    $pw = convertto-securestring -AsPlainText -Force -String "패스워드";
    $cred = new-object -typename System.Management.Automation.PSCredential -argumentlist "도메인\아이디",$pw
    $session = new-pssession -computername 서버명 -credential $cred
    
    Copy-Item E:\Jenkins\script\find.war -ToSession $session -Destination D:\-\Release\find.war  -PassThru
    ```
    

<https://talsu.net/?p=2108>

<https://self-interest.tistory.com/6>

<https://www.tutorialspoint.com/how-to-copy-files-folders-to-the-remote-location-in-the-powershell>

<https://lottogame.tistory.com/6521>

#### 폴더와 파일 생성

<https://www.delmaster.net/306>
