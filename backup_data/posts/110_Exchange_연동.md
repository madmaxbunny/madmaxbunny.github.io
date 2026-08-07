---
title: "Exchange 연동"
date: "2022-07-09T11:38:06+09:00"
category: "프로그래밍/JAVA"
tags: ["Exchange", "Independentsoft", "java"]
original_url: "https://priv.tistory.com/110"
tistory_id: 110
---

자바로 Exchange 연동 서비스를 개발하는 방법은 2가지 이다.

1\. OfficeDev의 ews-java-api 오픈 소스 사용

> <https://github.com/OfficeDev/ews-java-api>

2\. Independentsoft의 JWebServices 소스코드를 구매해서 개발

<https://independentsoft.de/jwebservices/index.html>

물론 EWS에서 API와 스팩을 제공하니, 직접 처음부터 개발해도 된다. 

하지만 1번 ews-java-api 오픈 소스를 보면 알겠지만 EWS-API의 무수히 많은 XML 파라매터를 패턴화 하는 코드양이 상당하니 가능하면 1번 2번 선택해서 개발하는게 좋을 것 같다. 

추가로 MS에서 EWS-API지원 중단이 된 건지 확인이 필요하다.

<https://devblogs.microsoft.com/microsoft365dev/upcoming-changes-to-exchange-web-services-ews-api-for-office-365/>

OfficeDev 에서도 2018년 이후 추가 업데이트가 없었다.

하지만 1, 2번 두 가지 방법 모두 지금까지 버전으로 Office365 온라인 메일 사서함까지 모두 연동이 가능하다. 

**1\. OfficeDev의 ews-java-api 오픈 소스 사용**

\- 간단하다. 가이드도 잘 나와 있다. 

<https://github.com/OfficeDev/ews-java-api/wiki/Getting-Started-Guide>

\- 메일 발송의 경우, 아래 처럼 작성하면 된다. 
    
    
    ```java
    package org.devlion.ews;
    
    import java.net.URI;
    import java.net.URISyntaxException;
    import java.util.EnumSet;
    
    import microsoft.exchange.webservices.data.core.ExchangeService;
    import microsoft.exchange.webservices.data.core.enumeration.misc.ConnectingIdType;
    import microsoft.exchange.webservices.data.core.enumeration.misc.ExchangeVersion;
    import microsoft.exchange.webservices.data.core.enumeration.misc.TraceFlags;
    import microsoft.exchange.webservices.data.core.service.item.EmailMessage;
    import microsoft.exchange.webservices.data.credential.ExchangeCredentials;
    import microsoft.exchange.webservices.data.credential.WebCredentials;
    import microsoft.exchange.webservices.data.misc.ITraceListener;
    import microsoft.exchange.webservices.data.misc.ImpersonatedUserId;
    import microsoft.exchange.webservices.data.property.complex.MessageBody;
    
    public class EwsTest {
    
    	String sender = "보내는 메일 주소";
    	ExchangeService service;
    
    	void init() throws URISyntaxException {
    		String exchangeUrl = "https://EWS주소/exchange.asmx";
    		String impersonationId = "서비스계정 ID";
    		String impersonationPw = "서비스계정 PW";
    
    		ExchangeCredentials credentials = new WebCredentials(impersonationId, impersonationPw);
    		service = new ExchangeService(ExchangeVersion.Exchange2010_SP2);
    		service.setUrl(new URI(exchangeUrl));
    		service.setCredentials(credentials);
    
    		// log
    		service.setTraceEnabled(true);
    		service.setTraceFlags(EnumSet.allOf(TraceFlags.class));
    		service.setTraceListener(new ITraceListener() {
    
    			public void trace(String traceType, String traceMessage) {
    				// do some logging-mechanism here
    				System.out.println("Type:" + traceType + " Message:" + traceMessage);
    			}
    		});
    
    	}
    
    	void send(String msg) throws Exception {
    		System.out.println("test()");
    
    		String reciver = "받는 메일 주소";
    
    		service.setImpersonatedUserId(new ImpersonatedUserId(ConnectingIdType.SmtpAddress, 
            sender));
    
    		EmailMessage emailMessage = new EmailMessage(service);
    		emailMessage.setSubject(msg);
    		emailMessage.setBody(MessageBody.getMessageBodyFromText("Sent using the EWS Java API."));
    		emailMessage.getToRecipients().add(reciver);
    		emailMessage.send();
    
    	}
    
    	public static void main(String[] args) throws Exception {
    		// TODO Auto-generated method stub
    		System.out.println("-start-");
    		EwsTest app = new EwsTest();
    		app.init();
    		app.send("Hello EWS!");
    		System.out.println("-done-");
    	}
    }
    ```
    

\- EWS 연동 XML 파라매터를 보기 위해 아래가 추가 되었다. 
    
    
    ```java
    // log
    service.setTraceEnabled(true);
    service.setTraceFlags(EnumSet.allOf(TraceFlags.class));
    service.setTraceListener(new ITraceListener() {
    
        public void trace(String traceType, String traceMessage) {
            // do some logging-mechanism here
            System.out.println("Type:" + traceType + " Message:" + traceMessage);
        }
    });
    ```
    

<https://github.com/OfficeDev/ews-java-api/wiki/HowTo%3A-Trace-Messages>

\- 사용자 패스워드를 입력 받지 않고 서비스 Admin 계정만으로 연동하기 위해 아래가 추가 되었다. 
    
    
    ```java
    service.setImpersonatedUserId(new ImpersonatedUserId(ConnectingIdType.SmtpAddress, sender));
    ```
    

\- Calendar는 아래처럼 연동하면 된다. 
    
    
    ```java
    	public void findAppointments() throws Exception {
    		
    		String exchangeUrl = "https://EWS주소/ews/exchange.asmx";
    		String impersonationId = "서비스계정 ID";
    		String impersonationPw = "서비스계정 PW";
    		String exchangeDomain = "도메인"; // (옵션)
    		
    		 ExchangeCredentials techUserCredential = new WebCredentials(impersonationId,
             impersonationPw, exchangeDomain);
    		 ExchangeService exchangeService = new ExchangeService(ExchangeVersion.Exchange2010_SP1);
    		 exchangeService.setCredentials(techUserCredential);
    		 exchangeService.setUrl(new URI(exchangeUrl));
    		 exchangeService.setImpersonatedUserId(
             new ImpersonatedUserId(ConnectingIdType.SmtpAddress, "메일주소"));
    		  
    		SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
    		Date startDate = formatter.parse("2022-06-01 12:00:00");
    		Date endDate = formatter.parse("2022-06-30 13:00:00");
    		
    		FolderId folderIdFromCalendar = new FolderId(WellKnownFolderName.Calendar, 
            Mailbox.getMailboxFromString("메일주소"));
    		CalendarFolder cf = CalendarFolder.bind(exchangeService, folderIdFromCalendar);
    		
    		FindItemsResults<Appointment> findResults = cf.findAppointments(
            new CalendarView(startDate, endDate));
    		for (Appointment appt : findResults.getItems()) {
    			appt.load(PropertySet.FirstClassProperties);
    			System.out.println("SUBJECT====="+appt.getSubject());
    			System.out.println("BODY========"+appt.getBody());
    		}
    	}
    ```
    

**2\. Independentsoft의 JWebServices 소스코드를 구매해서 개발**

\- [https://independentsoft.de/jwebservices/index.html](https://independentsoft.de/jwebservices/index.html%EF%BB%BF) 구매 필요

\- 저작권과 사내 보안 규정으로 소스코드를 공개하진 못한다. 이미 해당 코드를 구매해서 사용 중인 회사에서 참고하시면 좋을 것 같다. 

\- 소스코드에 약간의 문제가 있으며, 기본 제공 코드가 HttpConnection 재사용이 되질 않아 수정이 필요하다.

안드로이드 앱이나, 사내 Exchage 서버 주소가 1개라면 문제가 되지 않지만 여러 Exchage 서버를 운영 중인 회사라면 성능상 이슈가 발생할 수 있다. (특히, 해외 메일 서비스)

사내 Exchage 서버가 1대라면 기존 설정된 HttpClient 통신 라이브러리를 HttpURLConnection로 바꾸기만 하면 된다. 소스코드에 설정값으로 변경이 가능하도록 세팅이 되어 있으며, Service.java 상단에 옵션을 true로만 바꾸면 된다. 
    
    
    ```java
    //HttpURLConnection
    private boolean useHttpURLConnection = true; // 기본 값 : false
    ```
    

단, HttpURLConnection은 Connection pool을 지원하지 않으니, Exchage 서버 주소가 여러 대라면 기존 Connection을 끊지 못해 충돌이 발생하는 오류가 발생한다. 

이 경우, PoolingHttpClientConnectionManager 사용하도록 소스코드 수정이 필요하다. 

1) Service.java 파일의 setClientConnectionManager의 입력 파라매터가 HttpClientConnectionManager로 되어 있을텐데, PoolingHttpClientConnectionManager로 변경하고 connectionManager의 Max 값을 설정한다. 
    
    
    ```java
    connectionManager = new PoolingHttpClientConnectionManager(socketFactoryRegistry);
    connectionManager.setMaxTotal(10);
    connectionManager.setDefaultMaxPerRoute(10);
    ```
    

2) PoolingHttpClientConnectionManager을 Spring DI 또는 싱글톤으로 변경한다.

<https://www.hyoyoung.net/103>

3) NTCredentials을 사용한다면(Exchange 서버 이므로 당연히 모든 회사들이 사용할 듯), 아래 추가 조치만 해주면 된다.

<https://priv.tistory.com/109>
