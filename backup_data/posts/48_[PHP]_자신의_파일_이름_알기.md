---
title: "[PHP] 자신의 파일 이름 알기"
date: "2014-01-03T09:45:36+09:00"
category: "프로그래밍/Web"
tags: []
original_url: "https://priv.tistory.com/48"
tistory_id: 48
---

### 1\. 파일 이름 알기

<?  
$a = $_SERVER['PHP_SELF'];  
echo "$a";  
?>

### 2\. 확장자 제거하기

<?  
$b_array = explode(".",$_SERVER['PHP_SELF']); // '.'을 기준으로 문자열을 분류하여 배열에 저장  
echo "$b_array[0]";  
?>

### 3\. '/' 제거하기

<?  
$c_array = explode(".",$_SERVER['PHP_SELF']);  
$c = str_replace("/","",$c_array[0]); // '/'을 ''로 대체  
echo "$c";  
?>
