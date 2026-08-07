---
title: "[JAVA] 파일 합치기, 파일 삭제"
date: "2014-01-03T09:54:07+09:00"
category: "프로그래밍/JAVA"
tags: []
original_url: "https://priv.tistory.com/54"
tistory_id: 54
---

파일 합치기 
    
    
    ```
    import java.io.FileInputStream;
    import java.io.FileOutputStream;
    import java.io.IOException;
    
    public class test {
    	static String CONTENTS_DOWNLOAD_PATH = "";
    
    	public static void mergeFragment() {
    		String mergedContentsName = "server.zip";
    		int cnt = 183;
    		FileInputStream fis = null;
    		FileOutputStream fos = null;
    		try {
    			fos = new FileOutputStream(CONTENTS_DOWNLOAD_PATH
    					+ mergedContentsName);
    			byte[] buf = new byte[1024];
    			for (int fragmentCnt = 0; fragmentCnt < cnt; fragmentCnt++) {
    				System.out.println(">" + fragmentCnt + " 성공");
    				try {
    					int len = 0;
    					fis = new FileInputStream(CONTENTS_DOWNLOAD_PATH
    							+ mergedContentsName + fragmentCnt);
    					while ((len = fis.read(buf)) != -1) {
    						fos.write(buf, 0, len);
    					}
    					fos.flush();
    					fis.close();
    				} catch (IOException e) { // TODO Auto-generated catch block
    					e.printStackTrace();
    				}
    			}
    			fos.close();
    		} catch (IOException e1) { // TODO Auto-generated catch block
    			e1.printStackTrace();
    		}
    
    	}
    }
    
    
    ```
    

파일 삭제 
    
    
    ```
     
    import java.io.File;
    
    public class test {
    	static String CONTENTS_DOWNLOAD_PATH = "";
    
    	public static void deleteAllFragment() {
    		String mergedContentsName = "server.zip";
    		int cnt = 183;
    		File f = null;
    		for (int fragmentCnt = 0; fragmentCnt < cnt; fragmentCnt++) {
    			f = new File(CONTENTS_DOWNLOAD_PATH + mergedContentsName
    					+ fragmentCnt);
    			if (f.delete()) {
    				System.out.println(">" + fragmentCnt + " 삭제성공");
    			} else {
    				System.out.println(">" + fragmentCnt + " 삭제실패");
    			}
    		}
    	}
    }
    
    
    ```
    
