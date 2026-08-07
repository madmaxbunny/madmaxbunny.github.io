---
title: "[ReactNative] 배열 Map 반복"
date: 2021-04-28 23:52:23 +0900
categories: ["기타"]
tags: []
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
    
