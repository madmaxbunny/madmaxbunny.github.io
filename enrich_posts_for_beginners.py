import os
import re
import yaml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(BASE_DIR, '_posts')

EMOJIS = ["💡", "🚀", "📄", "📌", "⚙️", "🟢", "🔑", "🔍", "🛠️", "📑", "⚡️", "✨", "📝", "📢", "👉", "😊", "🎉", "📂", "📊", "🌐", "⏱️", "📑"]

def remove_emojis(text):
    for em in EMOJIS:
        text = text.replace(em, "")
    text = re.sub(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]', '', text)
    return text

BEGINNER_ENRICHMENTS = {
    '134': {
        'summary': 'IntelliJ IDEA에서 개발 생산성을 올리기 위한 자동 클래스 임포트(Auto Import)와 필수 단축키 세팅 가이드입니다.',
        'overview': """통합 개발 환경(IDE)인 IntelliJ IDEA는 코드를 작성할 때 보조 역할을 해주는 프로그램입니다.
자바(Java) 언어로 프로그래밍할 때 `import java.util.List;` 같은 패키지 경로를 일일이 손으로 입력하려면 오타가 나기 쉽고 시간이 오래 걸립니다.

Auto Import 기능을 활성화하면 작성 중인 클래스 이름을 알아차려 필요한 패키지를 자동으로 상단에 추가해주며, 사용하지 않는 패키지는 자동으로 정리해줍니다.""",
        'core': """### 1. Auto Import (자동 클래스 임포트) 설정

- **설정 경로**: `Settings` (`Ctrl + Alt + S` / Mac: `Cmd + ,`) ➔ `Editor` ➔ `General` ➔ `Auto Import`
- **주요 선택 항목 설명**:
  - `Add unambiguous imports on the fly`: 유일하게 존재하는 클래스 이름을 입력하면 자동으로 import 구문을 작성합니다.
  - `Optimize imports on the fly`: 코드를 수정하면서 더 이상 사용하지 않게 된 불필요한 import 구문을 자동으로 정리합니다.

### 2. 자주 사용하는 필수 단축키 목록

| 기능 | Windows / Linux | macOS | 설명 |
|---|---|---|---|
| 환경 설정 열기 | `Ctrl + Alt + S` | `Cmd + ,` | 설정 메뉴 창을 바로 엽니다. |
| 전체 파일/클래스 검색 | `Shift` 연속 2번 | `Shift` 연속 2번 | 프로젝트 내 모든 파일과 클래스를 검색합니다. |
| 최근 작업 파일 열기 | `Ctrl + E` | `Cmd + E` | 최근에 열어서 작업했던 파일 목록을 띄웁니다. |
| 코드 자동 정렬 | `Ctrl + Alt + L` | `Cmd + Option + L` | 삐뚤빼뚤한 코드 들여쓰기와 줄바꿈을 정돈합니다. |
| Import 수동 정리 | `Ctrl + Alt + O` | `Cmd + Option + O` | 불필요한 import 구문을 깔끔하게 정리합니다. |"""
    },
    '132': {
        'summary': '클라우드 가상 서버인 AWS EC2 인스턴스 접속부터 Nginx 웹 서버 및 Java, Tomcat 9 WAS 환경 구축 절차입니다.',
        'overview': """AWS EC2(Elastic Compute Cloud)는 인터넷상에서 빌려 쓰는 가상 서버(컴퓨터)입니다.
우리가 만든 웹 애플리케이션을 24시간 내내 사용자들이 접속할 수 있도록 하려면 클라우드 서버에 올리게 됩니다.

- **Nginx**: 사용자가 웹브라우저로 접속했을 때 가장 먼저 맞이해주는 대문(웹 서버) 역할입니다.
- **Tomcat**: 자바(Java)로 작성된 백엔드 서비스(WAS)를 실제로 실행시켜주는 엔진 역할입니다.""",
        'core': """### 1. EC2 원격 접속 및 Nginx 설치

```bash
# 1.1 비밀번호 대신 보안 키(.pem) 파일을 이용하여 원격 AWS 서버에 접속합니다.
sudo ssh -i jenkins.pem ec2-user@13.60.206.142

# 1.2 Nginx 웹 서버 패키지를 검색하고 최신 버전을 설치합니다.
amazon-linux-extras list | grep nginx
sudo amazon-linux-extras install -y nginx1

# 1.3 Nginx 서비스를 백그라운드에서 실행하고 상태를 확인합니다.
sudo systemctl start nginx
sudo systemctl status nginx
```

### 2. SSH Keygen 무암호 접속 설정

```bash
# 2.1 내 로컬 컴퓨터 터미널에서 RSA 방식의 보안 키 쌍(공개키, 개인키)을 생성합니다.
ssh-keygen -t rsa

# 2.2 생성된 id_rsa.pub (공개키) 파일 내용을 원격 EC2 서버의 ~/.ssh/authorized_keys 파일 끝에 추가합니다.
```

### 3. Java 8 & Tomcat 9 설치 및 서비스 등록

```bash
# 3.1 자바 실행 환경(Open-JDK 8)을 설치하고 버전을 확인합니다.
sudo yum install -y java-1.8.0-openjdk
java -version

# 3.2 Tomcat 9 설치 디렉토리를 생성하고 압축 파일을 다운로드받아 해제합니다.
sudo mkdir -p /opt/tomcat
sudo wget https://archive.apache.org/dist/tomcat/tomcat-9/v9.0.93/bin/apache-tomcat-9.0.93.tar.gz
sudo tar xvf apache-tomcat-9.0.93.tar.gz -C /opt/tomcat --strip-components=1
```"""
    },
    '130': {
        'summary': 'curl 명령어로 커스텀 Host 헤더를 지정하고 HTTP GET 요청으로 헬스체크 및 도메인 라우팅을 테스트하는 방법입니다.',
        'overview': """`curl`은 웹브라우저(Chrome) 없이 터미널 창에서 직접 특정 웹사이트 URL로 요청을 보내고 응답 결과를 테스트할 수 있는 명령어 도구입니다.

개발 시 도메인 연결(DNS)이 완결되지 않았거나 서버 내부에서 웹 응답이 올바르게 나오는지 검증할 때 curl 명령어를 사용합니다.""",
        'core': """### 1. curl 명령어 사용 예시 및 설명

```bash
# 커스텀 Host 헤더를 지정하고 SSL 검증을 무시한 채 GET 방식으로 웹 페이지를 요청합니다.
curl -k -H "Host: naver.com" -X GET "https://hkatwywawbp03/HealthCheck/IsAlive.htm"
```

- `-k` (`--insecure`): 개발 중 사설 인증서나 SSL 검증 오류가 발생해도 무시하고 연결을 진행합니다.
- `-H "Host: domain.com"`: HTTP 요청 헤더에 실제 서비스 도메인을 주입하여 Nginx나 IIS 가상 호스트 매칭을 테스트합니다.
- `-X GET`: 데이터를 읽어오는 HTTP GET 메서드 요청 방식으로 지정합니다."""
    },
    '125': {
        'summary': 'MS SQL Server에서 데이터베이스 LOCK(블로킹) 장애 발생 시 sp_who2 및 계층 쿼리로 원인 프로세스를 추적하고 해제하는 방법에 대한 노트입니다.',
        'overview': """데이터베이스에서 **LOCK(락)**이란 여러 작업이 동시에 하나의 데이터를 수정할 때 데이터가 꼬이지 않도록 순서를 세우는 안전장치입니다.

그러나 특정 프로그램이 락을 쥔 채 멈춰버리면 뒤에서 대기하던 다른 수십 개의 작업들이 전부 멈추는 장애가 발생합니다.
이 가이드는 원인 프로세스(SPID)를 찾아 연결을 끊어주는 대처 방법입니다.""",
        'core': """### 1. LOCK 확인 및 유발 프로세스 종료 쿼리

```sql
-- 1.1 현재 DB에서 실행 중인 프로세스 목록과 락 유발자(BlkBy)를 확인합니다.
EXEC SP_WHO2;

-- 1.2 락에 걸려 대기(BLOCKED > 0) 중인 프로세스만 필터링하여 조회합니다.
SELECT * FROM SYS.sysprocesses WHERE SPID > 50 AND BLOCKED > 0;

-- 1.3 락을 일으키고 있는 특정 SPID가 어떤 SQL 문장을 실행했는지 확인합니다.
DBCC INPUTBUFFER(123);

-- 1.4 락을 잡고 멈춰있는 123번 프로세스를 강제로 종료(Kill)하여 대기를 해제합니다.
KILL 123;
```

### 2. 락의 원인을 트리 구조로 추적하는 계층 쿼리

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
    },
    '124': {
        'summary': '네트워크 포트(Port)의 기본 개념과 자주 사용되는 주요 서비스별 포트 번호 모음집입니다.',
        'overview': """컴퓨터의 IP 주소가 '아파트 건물 주소'라면, **포트(Port)**는 아파트 내부의 '호수(방 번호)'와 같습니다.

컴퓨터 한 대 안에서는 웹서버, DB서버, 파일전송 서버 등 여러 서비스가 동시에 동작하는데, 외부에서 접속한 인터넷 신호가 어느 서비스로 찾아갈지 구분해주는 통로 번호가 바로 포트 번호입니다.""",
        'core': """### 자주 사용되는 대표 포트 번호 목록

| 포트 번호 | 서비스 / 프로토콜 | 설명 |
|---|---|---|
| `21` | FTP | 파일 송수신 전용 포트 |
| `22` | SSH | 원격 보안 터미널 접속 포트 |
| `23` | Telnet | 암호화되지 않은 옛날 원격 접속 포트 |
| `80` | HTTP | 일반 웹사이트 접속 포트 |
| `443` | HTTPS | 보안 암호화(SSL)가 적용된 웹사이트 접속 포트 |
| `1433` | MS-SQL | MS SQL Server 데이터베이스 기본 포트 |
| `3306` | MySQL | MySQL 데이터베이스 기본 포트 |
| `8080` | Web/WAS | 개발용 웹 서버 및 Tomcat 기본 포트 |"""
    }
}

def clean_markdown_codeblocks(text):
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

def process_file(filepath):
    filename = os.path.basename(filepath)
    m = re.search(r'^\d{4}-\d{2}-\d{2}-(\d+)-', filename)
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

    title_clean = remove_emojis(str(meta.get('title', 'Post'))).strip()
    meta['title'] = title_clean

    info = BEGINNER_ENRICHMENTS.get(pid, {})
    summary = info.get('summary', f'{title_clean}의 기본 개념과 실무 적용 명령어를 대학교 1학년 눈높이에 맞춰 정리한 기술 노트입니다.')
    overview = info.get('overview', f'{title_clean}은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 초보자 분들도 쉽게 이해할 수 있도록 기본 용어 개념과 배경 지식을 먼저 설명하고, 실제 적용 코드와 실행법을 차근차근 다룹니다.')

    if 'core' in info:
        core_content = info['core']
    else:
        # Strip old duplicate headings or callout blocks if present
        clean_body = re.sub(r'>\s*\*\*\[핵심 요약\]\*\*[^\n]*\n*', '', body)
        clean_body = re.sub(r'#+\s*(\d+\.\s*)?개요.*', '', clean_body)
        clean_body = re.sub(r'#+\s*(\d+\.\s*)?핵심.*', '', clean_body)
        clean_body = re.sub(r'#+\s*(\d+\.\s*)?정리.*', '', clean_body)
        clean_body = clean_markdown_codeblocks(remove_emojis(clean_body)).strip()
        core_content = clean_body

    # Build clean non-duplicated beginner post structure
    new_body = f"""> **[핵심 요약]**
> {summary}

---

## 1. 개요 및 배경

{overview}

---

## 2. 핵심 설명 및 코드

{core_content}

---

## 3. 정리하며

이상으로 {title_clean}의 기초 개념과 실행 방법에 대한 공유를 마칩니다.
"""

    if '{{' in new_body or '{%' in new_body:
        if '{% raw %}' not in new_body:
            new_body = "{% raw %}\n" + new_body.strip() + "\n{% endraw %}"

    new_body = re.sub(r'\n{3,}', '\n\n', new_body)
    new_fm = yaml.dump(meta, allow_unicode=True, sort_keys=False).strip()
    new_file_content = f"---\n{new_fm}\n---\n{new_body}"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_file_content)

def main():
    enriched_count = 0
    for f in sorted(os.listdir(POSTS_DIR)):
        if f.endswith('.md'):
            process_file(os.path.join(POSTS_DIR, f))
            enriched_count += 1
    print(f"Successfully processed and enriched {enriched_count} existing post files in _posts/!")

if __name__ == '__main__':
    main()
