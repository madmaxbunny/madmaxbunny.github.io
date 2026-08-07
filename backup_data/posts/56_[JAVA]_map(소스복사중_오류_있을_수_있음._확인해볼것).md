---
title: "[JAVA] map(소스복사중 오류 있을 수 있음. 확인해볼것)"
date: "2014-01-03T10:11:41+09:00"
category: "프로그래밍/JAVA"
tags: []
original_url: "https://priv.tistory.com/56"
tistory_id: 56
---


    ```
    
    import java.util.ArrayList;
    import java.util.HashMap;
    import java.util.Map;
    
    public class test {
    	static Map map = new HashMap();
    
    	public static void main(String[] args) {
    		insert("a", "1");
    		insert("b", "2");
    		insert("c", "3");
    		insert("a", "1");
    		insert("b", "2");
    		insert("c", "3");
    		insert("d", "3");
    		System.out.println(map);
    	}
    
    	static void insert(String key, String val) {
    		ArrayList c = map.get(key);
    		if (null == c) {
    			c = new ArrayList();
    		}
    		c.add(val);
    		map.put(key, c);
    	}
    }
    
    ```
    
