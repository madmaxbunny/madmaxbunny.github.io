---
title: "[ReactNative] 배열 Map 반복"
date: "2021-04-28T23:52:23+09:00"
category: "카테고리 없음"
tags: []
original_url: "https://priv.tistory.com/105"
tistory_id: 105
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
    
