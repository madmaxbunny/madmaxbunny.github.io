---
title: "[Node] express"
date: "2021-06-28T20:14:31+09:00"
category: "카테고리 없음"
tags: ["express", "node"]
original_url: "https://priv.tistory.com/106"
tistory_id: 106
---

1\. 설치
    
    
    ```javascript
    > npm install express --save
    ```
    

2\. app.js
    
    
    ```javascript
    const express = require('express')
    const app = express()
    const port = 3000
    
    
    app.use(express.static(__dirname + '/web'));
    
    app.listen(port, () => {
      console.log("server running... ");
    })
    ```
    

3\. 실행
    
    
    ```javascript
    > node app.js
    ```
    
