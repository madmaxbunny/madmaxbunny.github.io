---
title: "ElasticSearch"
date: 2022-11-05 23:04:36 +0900
categories: ["프로그래밍", "기타"]
tags: []
---

> **[핵심 요약]**
> ElasticSearch 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트이에요.

---

## 1. 개요 및 배경

ElasticSearch과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유해요.

---

## 2. 핵심 설명 및 코드

### **1\. 설치**
    
    
```bash
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.10.0
docker run -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.10.0
```
    

* * *

#### **버전확인**
    
    
```bash
GET /
```
    

### 

### **2\. CRUD**
    
    
```bash
http://<호스트>:<포트>/<인덱스>/_doc/<도큐먼트 id>
```
    

#### **1) 상태 확인**
    
    
```bash
#index 조회
GET /_cat/indices?v 

#상태확인
GET /_cat/health?v
```
    

#### **2) 삽입**
    
    
```bash
PUT /movie/_doc/1

{
    "msg" : "Hello Elasticsearch!"
}
```
    

#### **3) 조회**
    
    
```bash
# 단일검색
GET /movie/_doc/1

# 모든 문서 검색
GET /movie/_search

# 조건 검색
GET /movie/_search?q=hello
GET /movie/_search?q=hello OR hi
```
    

#### **3) 삭제**
    
    
```bash
#index 삭제
DELETE /movie

#doc 삭제(_id). DELETE /INDEX/TYPE/_id
DELETE /movie/_doc/4

#doc 삭제(쿼리). POST /INDEX/_delete_by_query
DELETE /movie/_delete_by_query
{
	"query" : {
		"match" : {
			"msg" : "hello"
		}
	}
}
```
    

* * *

#### 3\. 집계 함수

#### 1) group by
    
    
```javascript
GET gw-heartbeat/_search
{
  "size": 0,
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "@timestamp": {
              "gt": "2023-01-19T00:00:00.000Z",
              "lt": "2023-01-20T00:00:00.000Z"
            }
          }
        }
      ]
    }
  },
  "aggs": {
    "count": {
      "terms": {
        "field": "url.domain",
        "size" : 1000
        
      }
    }
  }
}
```
    

#### 2) group by (필드 2개 이상)
    
    
```javascript
GET gw-heartbeat/_search
{
  "size": 0,
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "@timestamp": {
              "gt": "2023-01-19T00:00:00.000Z",
              "lt": "2023-01-20T00:00:00.000Z"
            }
          }
        }
      ]
    }
  },
  "aggs": {
    "myName": {
      "multi_terms" : {
        "terms" : [
          {"field": "url.domain"},
          {"field": "monitor.ip"}
        ],
        "size" : 1000
      }
    }
  }
}
```
    

4\. 예제

AND 조건, Timezone
    
    
```javascript
{
  "track_total_hits": true,
  "query": {
    "bool": {
      "filter": [
        {
          "match": {
            "tags": "GRHQ"
          }
        },
        {
          "match": {
            "tags": "MO"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": "2023-05-01T00:00:00.000",
              "lte": "2023-05-25T00:00:00.000",
              "time_zone": "Asia/Seoul"
            }
          }
        }
      ]
    }
  },
  "aggs": {
    "avg": {
      "avg": {
        "field": "time_taken"
      }
    }
  }
}
```
    

  * 전체 범위 검색을 하려면 "track_total_hits": true 작성해야 함
  * 불필요한 데이터가 많이 보일 때는 ?size=0 적용
  * Timezone 적용할 때, 2023-05-21T00:00:00.000Z 이런식으로 뒤에 Z가 붙으면 적용이 안됨
  * 카운트를 계산할 때는 집계 보다는 /_count가 간단함. => discover에서 작성하는게 더 빠를 듯
  * avg 추출 했더니, 결과에 count도 함께 나온다.

OR 조건
    
    
```javascript
GET gw-http-accesslog/_count
{
  "query": {
    "bool": {
      "filter": [
        {
          "bool": {
            "should": [
              {
                "match": {
                  "tags": "GRHQ"
                }
              },
              {
                "match": {
                  "tags": "MO"
                }
              }
            ]
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": "2023-05-24T20:00:00.000",
              "lte": "2023-05-24T20:00:00.001",
              "time_zone": "Asia/Seoul"
            }
          }
        }
      ]
    }
  }
}
```
    

<https://coralogix.com/blog/42-elasticsearch-query-examples-hands-on-tutorial/>

<https://esbook.kimjmin.net/05-search/5.2-bool>

<https://stackoverflow.com/questions/57392532/elasticsearch-how-to-write-an-or-clause-in-filter-context>

<https://victorydntmd.tistory.com/314>

---

## 3. 정리하며

관련해서 궁금하신 점이나 나눠보고 싶은 의견이 있다면 댓글로 편하게 말씀해주세요.
