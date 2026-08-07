---
title: "[JAVA] timer"
date: "2014-01-03T09:59:33+09:00"
category: "프로그래밍/JAVA"
tags: []
original_url: "https://priv.tistory.com/55"
tistory_id: 55
---


    ```
    
    import java.util.Timer;
    import java.util.TimerTask;
    
    public class test {
    	public static void main(String[] args) {
    		Timer timer = new Timer();
    		timer.schedule(new WorkTask(), 5000); // 5초후에 실행
    		timer.schedule(new WorkTask(), 5000, 3000); // 5초후에 3초 간격으로 실행
    	}
    
    	public static class WorkTask extends TimerTask {
    		@Override
    		public void run() {
    			System.out.println("Timer.");
    		}
    
    	}
    }
    
    ```
    
