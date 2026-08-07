---
title: "Prometheus & Grafana"
date: 2024-06-07 23:52:56 +0900
categories: ["기타"]
tags: ["그라파나", "프로메테우스"]
---

ELK와 같은 데이터 시각화 툴

\-- 메모 --

## 1\. Prometheus

Windows OS에서 Prometheus 실행 방법
    
    
    ```bash
    prometheus.exe --config.file=prometheus.yml --web.listen-address=:9090
    ```
    

Prometheus 기본 설명

<https://blog.naver.com/alice_k106/221535163599>

<https://devthomas.tistory.com/15>

## 2\. Grafana

Grafana 대시보드 다운로드

<https://grafana.com/grafana/dashboards/>

스프링 부트 연동 및 커스텀 데이터 생성

<https://acafela.github.io/monitoring/2021/11/28/prometheus-grafana-springboot-1.html>

3\. Spring Boot 연동

<https://hstory0208.tistory.com/entry/PrometheusSpring-%ED%94%84%EB%A1%9C%EB%A9%94%ED%85%8C%EC%9A%B0%EC%8A%A4%EC%99%80-%EC%8A%A4%ED%94%84%EB%A7%81-%EC%97%B0%EA%B2%B0>

이슈 사항 - Springfox

<https://hudi.blog/spring-boot-actuator-prometheus-grafana-set-up/>
