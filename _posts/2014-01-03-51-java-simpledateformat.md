---
title: "[JAVA] SimpleDateFormat"
date: 2014-01-03 09:51:34 +0900
categories: ["프로그래밍", "JAVA"]
tags: []
---


    ```
    
    import java.text.SimpleDateFormat; 
    import java.util.Date; 
    import java.util.Calendar; 
    import java.util.TimeZone; 
      
    public class test { 
        public static void main(String[] args) { 
      
            System.out.println(getCurrentDateTime()); 
        } 
          
        static String getCurrentDateTime() { 
            SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss.ms"); 
            Date dateTime = new Date(); 
            TimeZone tz = TimeZone.getTimeZone("Asia/Seoul"); 
            sdf.setTimeZone(tz); 
      
            return sdf.format(dateTime); 
        } 
    }
    
    ```
    
