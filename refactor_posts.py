import os
import re
import yaml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(BASE_DIR, '_posts')

ENRICHMENTS = {
    '134': {
        'tldr': 'IntelliJ IDEA에서 자주 사용하는 핵심 설정인 자동 임포트(Auto Import), 단축키 및 생산성 향상 옵션 가이드입니다.',
        'overview': 'IntelliJ IDEA를 새로 설치하거나 프로젝트 세팅 시 매번 찾아보는 핵심 필수 설정 모음입니다. 특히 클래스 참조 시 자동으로 import 패키지를 추가해 주는 설정은 백엔드 개발 생산성을 극대화합니다.',
        'section_core': """### 1. Auto Import (자동 패스워드/클래스 임포트)
- **설정 경로**: `Settings` (`Ctrl + Alt + S` / Mac: `Cmd + ,`) ➔ `Editor` ➔ `General` ➔ `Auto Import`
- **주요 체크 항목**:
  - `Add unambiguous imports on the fly`: 유일한 패키지 클래스 작성 시 자동으로 import 문 추가
  - `Optimize imports on the fly`: 코드 수정 시 사용하지 않는 불필요한 import 구문 자동 제거

### 2. 자주 사용하는 단축키 모음
| 동작 | Windows / Linux | macOS |
|---|---|---|
| 설정 열기 | `Ctrl + Alt + S` | `Cmd + ,` |
| 클래스 / 파일 검색 | `Double Shift` | `Double Shift` |
| 최근 연 파일 | `Ctrl + E` | `Cmd + E` |
| 코드 자동 정렬 | `Ctrl + Alt + L` | `Cmd + Option + L` |
| 사용하지 않는 Import 정리 | `Ctrl + Alt + O` | `Cmd + Option + O` |"""
    },
    '130': {
        'tldr': 'curl 명령어를 활용하여 커스텀 Host 헤더를 설정하고 HTTP GET 요청으로 헬스체크(Health Check) 및 도메인 라우팅을 테스트하는 방법입니다.',
        'overview': '개발 및 인프라 운용 중 로드밸런서(ALB/ELB)나 Nginx 프록시 전면에서 내부 IP로 직접 요청을 보낼 때, Host 헤더를 도메인으로 지정하여 가상 호스트(Virtual Host) 동작을 검증해야 하는 경우가 자주 발생합니다.',
        'section_core': """### 1. 주요 명령어 및 옵션 설명
```bash
curl -k -H "Host: naver.com" -X GET "https://hkatwywawbp03/HealthCheck/IsAlive.htm"
```

- `-k` (`--insecure`): Self-signed 사설 인증서 또는 인증서 검증 오류를 무시하고 SSL/TLS 접속 허용
- `-H "Host: domain.com"`: HTTP 요청 헤더에 실제 서비스 도메인을 강제로 주입 (Nginx/IIS 가상호스트 매칭용)
- `-X GET`: 요청 방식을 GET 메서드로 지정

### 2. 실무 활용 시나리오
1. **DNS 변경 전 로컬 프록시 테스트**: DNS 변경 전 특정 웹 서버가 올바른 도메인 응답을 주는지 검증
2. **Internal Health Check**: L4/L7 스위치나 Nginx 전면에서 내부에 위치한 WAS 헬스체크 URL 응답 확인"""
    },
    '132': {
        'tldr': 'AWS EC2 인스턴스 생성 후 SSH 접속, Nginx 웹 서버 및 Java 8, Tomcat 9 WAS 설치 및 서비스 등록까지의 전체 인프라 구축 절차입니다.',
        'overview': 'AWS EC2 (Amazon Linux 2 / Linux 2023) 인스턴스를 최초 할당받은 후 개발 및 웹 서비스를 위한 웹 서버(Nginx)와 웹 애플리케이션 서버(Tomcat 9), Java 8 환경을 올바르게 구축하는 가이드입니다.',
        'section_core': """### 1. EC2 접속 및 Nginx 설치
```bash
# 1.1 PEM 키를 이용한 SSH 접속
sudo ssh -i jenkins.pem ec2-user@13.60.206.142

# 1.2 Nginx 패키지 확인 및 설치
amazon-linux-extras list | grep nginx
sudo amazon-linux-extras install -y nginx1
sudo systemctl start nginx
sudo systemctl status nginx
```

### 2. SSH Keygen을 활용한 비밀번호/PEM 키 없는 무암호 접속
```bash
# 로컬 PC에서 SSH 키 생성
ssh-keygen -t rsa
# 생성된 ~/.ssh/id_rsa.pub 파일의 공계키 내용을 원격 EC2의 ~/.ssh/authorized_keys 파일에 추가
```

### 3. Java 8 & Tomcat 9 설치 및 서비스 등록
```bash
# Java 8 설치
sudo yum install -y java-1.8.0-openjdk
java -version

# Tomcat 9 다운로드 및 압축 해제
sudo mkdir -p /opt/tomcat
sudo wget https://archive.apache.org/dist/tomcat/tomcat-9/v9.0.93/bin/apache-tomcat-9.0.93.tar.gz
sudo tar xvf apache-tomcat-9.0.93.tar.gz -C /opt/tomcat --strip-components=1
```

### 4. Tomcat systemd 서비스 파일 설정 (`/etc/systemd/system/tomcat.service`)
```ini
[Unit]
Description=Apache Tomcat Web Application Container
After=syslog.target network.target

[Service]
Type=forking
Environment=JAVA_HOME=/usr/lib/jvm/jre
Environment=CATALINA_PID=/opt/tomcat/temp/tomcat.pid
Environment=CATALINA_HOME=/opt/tomcat
Environment=CATALINA_BASE=/opt/tomcat
Environment='CATALINA_OPTS=-Xms512M -Xmx1024M -server -XX:+UseParallelGC'
Environment='JAVA_OPTS=-Djava.awt.headless=true -Djava.security.egd=file:/dev/./urandom'
ExecStart=/opt/tomcat/bin/startup.sh
ExecStop=/opt/tomcat/bin/shutdown.sh
User=tomcat
Group=tomcat
UMask=0007
RestartSec=10
Restart=always

[Install]
WantedBy=multi-user.target
```"""
    },
    '125': {
        'tldr': 'MS SQL Server에서 발생한 데이터베이스 LOCK(블로킹) 장애 발생 시 sp_who2 및 계층 쿼리를 사용해 부모 LOCK 유발 프로세스를 추적하고 해제하는 방법입니다.',
        'overview': 'MS SQL 운영 중 특정 트랜잭션이 테이블 락을 잡고 있어 후속 쿼리들이 모두 대기(SUSPENDED) 상태로 정체되는 장애 상황에서 빠른 응급 조치 및 원인 쿼리 추출 방법입니다.',
        'section_core': """### 1. 빠른 LOCK 확인 및 프로세스 종료 (Kill)
```sql
-- 1. LOCK 확인: BlkBy 컬럼에 값이 있는 프로세스 확인
EXEC SP_WHO2;

-- 2. BLOCKED > 0 인 프로세스 조회
SELECT * FROM SYS.sysprocesses WHERE SPID > 50 AND BLOCKED > 0;

-- 3. 유발 쿼리 텍스트 상세 보기
DBCC INPUTBUFFER([SPID]);

-- 4. Lock 걸린 프로세스 강제 종료
KILL [SPID];
```

### 2. 계층 쿼리(CTE Recursive)를 활용한 부모 ROOT LOCK 탐색
sp_who2의 결과를 계층 구조로 추적하여 최상위 원인 프로세스를 찾는 CTE 쿼리입니다:
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

def process_file(filepath):
    filename = os.path.basename(filepath)
    m = re.search(r'-(\d+)-', filename)
    pid = m.group(1) if m else None

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split('---', 2)
    if len(parts) < 3:
        return

    frontmatter_raw = parts[1]
    body = parts[2].strip()

    try:
        meta = yaml.safe_load(frontmatter_raw)
    except Exception:
        meta = {}

    title = meta.get('title', 'Post')

    # Get enrichment info if available
    enrichment = ENRICHMENTS.get(pid, {})
    tldr = enrichment.get('tldr', f'{title}에 대한 상세 설명 및 핵심 가이드입니다.')
    overview = enrichment.get('overview', f'{title} 가이드 및 실무 적용 설명입니다.')
    section_core = enrichment.get('section_core', body)

    # Rebuild Markdown with Style Guide Layout
    new_body = f"""
> 💡 **TL;DR (핵심 요약)**  
> {tldr}

---

## 1. 개요 및 배경

{overview}

---

## 2. 핵심 설정 및 실행 가이드

{section_core}

---

## 3. 요약 및 참고사항

- 본 포스트는 실무 개발 및 인프라 운용 중 검증된 노하우를 바탕으로 정리되었습니다.
- 추가 문의나 개선사항은 포스트 하단 댓글 또는 GitHub 이슈로 전달해 주세요.
"""

    # Liquid tag escaping check
    if '{{' in new_body or '{%' in new_body:
        if '{% raw %}' not in new_body:
            new_body = "{% raw %}\n" + new_body.strip() + "\n{% endraw %}"

    new_file_content = f"---{frontmatter_raw}---\n{new_body}"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_file_content)
    print(f"[{pid}] Revamped {filename}")

def main():
    print("Revamping all blog posts in _posts/ according to Optimization Style Guide...")
    for f in sorted(os.listdir(POSTS_DIR)):
        if f.endswith('.md'):
            process_file(os.path.join(POSTS_DIR, f))
    print("Completed post revamping successfully!")

if __name__ == '__main__':
    main()
