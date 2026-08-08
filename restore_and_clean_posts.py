import os
import re
import json
import yaml
import shutil
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKUP_DIR = os.path.join(BASE_DIR, 'backup_data')
POSTS_DIR = os.path.join(BASE_DIR, '_posts')

EMOJIS = ["💡", "🚀", "📄", "📌", "⚙️", "🟢", "🔑", "🔍", "🛠️", "📑", "⚡️", "✨", "📝", "📢", "👉", "😊", "🎉", "📂", "📊", "🌐", "⏱️", "📑"]

def remove_emojis(text):
    for em in EMOJIS:
        text = text.replace(em, "")
    text = re.sub(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]', '', text)
    return text

def sanitize_slug(text):
    text = re.sub(r'[^\w\s-]', '', text, flags=re.UNICODE)
    text = re.sub(r'[\s_]+', '-', text).strip('-').lower()
    return text[:40] if text else 'post'

# Specific clean explanations for key technical posts
CLEAN_EXPLANATIONS = {
    '134': {
        'summary': 'IntelliJ IDEA에서 개발 생산성을 올리기 위한 자동 클래스 임포트(Auto Import)와 필수 단축키 세팅 가이드이에요.',
        'intro': 'IntelliJ IDEA를 새로 설치하거나 프로젝트를 구성할 때 매번 찾아보는 핵심 필수 설정을 정리해봤어요.',
        'content': """### Auto Import (자동 클래스 임포트)
- **설정 경로**: `Settings` (`Ctrl + Alt + S` / Mac: `Cmd + ,`) ➔ `Editor` ➔ `General` ➔ `Auto Import`
- **주요 선택 항목**:
  - `Add unambiguous imports on the fly`: 사용 중인 클래스 작성 시 자동으로 import 구문을 추가해줘요.
  - `Optimize imports on the fly`: 코드 수정 시 사용하지 않는 불필요한 import 구문을 자동으로 정리해줘요.

### 자주 사용하는 필수 단축키
| 기능 | Windows / Linux | macOS |
|---|---|---|
| 환경 설정 | `Ctrl + Alt + S` | `Cmd + ,` |
| 전체 검색 | `Double Shift` | `Double Shift` |
| 최근 파일 열기 | `Ctrl + E` | `Cmd + E` |
| 코드 자동 정렬 | `Ctrl + Alt + L` | `Cmd + Option + L` |
| Import 정리 | `Ctrl + Alt + O` | `Cmd + Option + O` |"""
    },
    '130': {
        'summary': 'curl 명령어로 커스텀 Host 헤더를 지정하고 HTTP GET 요청으로 헬스체크 및 도메인 라우팅을 테스트하는 방법이에요.',
        'intro': '로드밸런서 전면이나 Nginx 프록시 환경에서 내부 IP로 직접 요청을 보낼 때, 커스텀 Host 헤더로 가상 호스트 동작을 테스트한 경험을 정리해봤어요.',
        'content': """### 사용 명령어 및 옵션
```bash
curl -k -H "Host: naver.com" -X GET "https://hkatwywawbp03/HealthCheck/IsAlive.htm"
```

- `-k` (`--insecure`): 인증서 검증 오류나 사설 SSL 인증서를 무시하고 접속해요.
- `-H "Host: domain.com"`: HTTP 요청 헤더에 서비스 도메인을 주입하여 가상호스트 매칭을 검증해요.
- `-X GET`: GET 메서드로 요청을 전송해요."""
    },
    '132': {
        'summary': 'AWS EC2 인스턴스 접속부터 Nginx 설치, SSH 키젠 무암호 접속 및 Java 8, Tomcat 9 WAS 환경 구축 절차이에요.',
        'intro': 'AWS EC2 인스턴스를 최초 생성한 후 개발 및 웹 서비스를 위해 Nginx, Tomcat 9, Java 8 환경을 구축했던 과정을 정리해봤어요.',
        'content': """### 1. EC2 접속 및 Nginx 설치
```bash
# 1.1 PEM 키를 이용한 SSH 접속
sudo ssh -i jenkins.pem ec2-user@13.60.206.142

# 1.2 Nginx 설치 및 실행
amazon-linux-extras list | grep nginx
sudo amazon-linux-extras install -y nginx1
sudo systemctl start nginx
sudo systemctl status nginx
```

### 2. SSH Keygen 무암호 접속 설정
```bash
# 로컬 PC에서 SSH 키 생성
ssh-keygen -t rsa
# 생성된 ~/.ssh/id_rsa.pub 공공키 내용을 원격 EC2의 ~/.ssh/authorized_keys 파일에 추가해요.
```

### 3. Java 8 & Tomcat 9 설치 및 서비스 등록
```bash
# Java 8 설치
sudo yum install -y java-1.8.0-openjdk
java -version

# Tomcat 9 다운로드 및 설정
sudo mkdir -p /opt/tomcat
sudo wget https://archive.apache.org/dist/tomcat/tomcat-9/v9.0.93/bin/apache-tomcat-9.0.93.tar.gz
sudo tar xvf apache-tomcat-9.0.93.tar.gz -C /opt/tomcat --strip-components=1
```"""
    },
    '125': {
        'summary': 'MS SQL Server에서 데이터베이스 LOCK(블로킹) 장애 발생 시 sp_who2 및 계층 쿼리로 원인 프로세스를 추적하고 해제하는 방법에 대한 노트이에요.',
        'intro': 'MS SQL 운영 중 특정 트랜잭션이 테이블 락을 잡고 있어 서비스 응답이 정체되었을 때 빠르게 원인을 찾아 조치한 경험을 정돈해봤어요.',
        'content': """### 1. LOCK 확인 및 유발 프로세스 조치
```sql
-- 1. LOCK을 걸고 있는 프로세스 확인 (BlkBy 컬럼 확인)
EXEC SP_WHO2;

-- 2. BLOCKED가 0보다 큰 대기 프로세스 조회
SELECT * FROM SYS.sysprocesses WHERE SPID > 50 AND BLOCKED > 0;

-- 3. 유발 쿼리 텍스트 상세 확인
DBCC INPUTBUFFER([SPID]);

-- 4. 락 유발 프로세스 강제 종료
KILL [SPID];
```

### 2. 계층 쿼리(CTE Recursive)를 활용한 부모 ROOT LOCK 추적
```sql
WITH tree_table AS (
    SELECT SPID id, IIF(BlkBy = '  .', 0, CAST(BlkBy AS INT)) parent_id, SPID name
    FROM #temp_sp_who2 
), tree_query AS (
    SELECT id, parent_id, name, CAST(id AS VARCHAR(255)) sort, CAST(name AS VARCHAR(255)) depth_fullname
    FROM tree_table WHERE parent_id = 0
    UNION ALL
    SELECT B.id, B.parent_id, B.name, CAST(C.sort + ' > ' + CAST(B.id AS VARCHAR) AS VARCHAR(255)), CAST(C.depth_fullname + ' > ' + CAST(B.name AS VARCHAR) AS VARCHAR(255))
    FROM tree_table B JOIN tree_query C ON B.parent_id = C.id
)
SELECT id, parent_id, name, depth_fullname FROM tree_query WHERE parent_id != 0 ORDER BY sort;
```"""
    }
}

def clean_markdown_codeblocks(text):
    # Unindent codeblocks
    lines = text.split('\n')
    cleaned = []
    in_cb = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('```'):
            in_cb = not in_cb
            cleaned.append(stripped)
        elif in_cb:
            if line.startswith('    '):
                cleaned.append(line[4:])
            elif line.startswith('\t'):
                cleaned.append(line[1:])
            else:
                cleaned.append(line)
        else:
            cleaned.append(line)
    return '\n'.join(cleaned)

def restore_and_build_clean_posts():
    with open(os.path.join(BACKUP_DIR, 'knowledge_base.json'), 'r', encoding='utf-8') as f:
        posts = json.load(f)

    # Wipe current _posts directory to prevent any old duplicated files
    if os.path.exists(POSTS_DIR):
        shutil.rmtree(POSTS_DIR)
    os.makedirs(POSTS_DIR, exist_ok=True)

    restored_count = 0
    for item in posts:
        pid = str(item['id'])
        title_raw = item['title']
        title_clean = remove_emojis(title_raw).strip()
        categories = [remove_emojis(c).strip() for c in item['category'].split('/') if c.strip()][:2]
        if not categories:
            categories = ["개발노트"]

        raw_date = item['date']
        try:
            dt = datetime.fromisoformat(raw_date)
            formatted_date = dt.strftime("%Y-%m-%d %H:%M:%S +0900")
            day_str = dt.strftime("%Y-%m-%d")
        except Exception:
            formatted_date = "2024-01-01 00:00:00 +0900"
            day_str = "2024-01-01"

        slug = sanitize_slug(title_clean)
        filename = f"{day_str}-{pid}-{slug}.md"

        # Check clean explanation override or use original markdown content
        custom_info = CLEAN_EXPLANATIONS.get(pid, {})
        summary = custom_info.get('summary', f'{title_clean} 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트이에요.')
        intro = custom_info.get('intro', f'{title_clean}과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유해요.')
        
        if 'content' in custom_info:
            core_content = custom_info['content']
        else:
            # Clean original markdown from knowledge_base
            orig_md = item['markdown'].replace('../images/', '/assets/img/posts/')
            orig_md = remove_emojis(orig_md)
            orig_md = clean_markdown_codeblocks(orig_md)
            core_content = orig_md.strip()

        # Build clean non-duplicated markdown structure
        body = f"""> **[핵심 요약]**
> {summary}

---

## 1. 개요 및 배경

{intro}

---

## 2. 핵심 설명 및 코드

{core_content}

---

## 3. 정리하며

관련해서 궁금하신 점이나 나눠보고 싶은 의견이 있다면 댓글로 편하게 말씀해주세요.
"""

        # Wrap Liquid tags safely
        if '{{' in body or '{%' in body:
            if '{% raw %}' not in body:
                body = "{% raw %}\n" + body.strip() + "\n{% endraw %}"

        body = re.sub(r'\n{3,}', '\n\n', body)

        frontmatter = f"""---
title: "{title_clean.replace('"', '\\"')}"
date: {formatted_date}
categories: {json.dumps(categories, ensure_ascii=False)}
tags: []
---

"""
        filepath = os.path.join(POSTS_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(frontmatter + body)
        restored_count += 1

    print(f"Successfully restored and built {restored_count} clean, non-duplicated posts!")

if __name__ == '__main__':
    restore_and_build_clean_posts()
