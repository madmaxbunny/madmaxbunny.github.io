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

PRECISE_SUMMARIES = {
    '2': '선형 디오판토스 방정식(Linear Diophantine Equation)의 정수해를 구하는 확장 유클리드 알고리즘 구현입니다.',
    '3': 'C언어를 활용하여 4X8 자물쇠의 암호키 조합을 생성하고 매칭을 검증하는 알고리즘 코드입니다.',
    '5': '단일 연결 리스트(Single Linked List)에서 신규 노드를 순서대로 정렬하여 삽입하는 알고리즘 구현입니다.',
    '9': 'C언어 포인터 배열을 함수 인자로 전달하여 참조에 의한 호출(Call by Reference)을 수행하는 예제입니다.',
    '12': '중앙대학교 인적 정보 명함 데이터를 저장하고 관리하기 위한 C언어 구조체 및 데이터 처리 코드입니다.',
    '13': '동아리 뱃지 및 회원 관리를 위한 텍스트 처리 C언어 프로그램 노트입니다.',
    '14': '동적 메모리 할당을 통해 이진 트리(Binary Tree) 노드를 생성하고 트리의 구조를 다루는 C언어 알고리즘입니다.',
    '15': '0이 대부분인 희소행렬(Sparse Matrix)을 이진 트리를 활용하여 효율적으로 전치(Transpose)하는 알고리즘입니다.',
    '16': '배열과 포인터를 활용해 다항식을 입력받고 학번 조건에 맞는 곱셈 결과를 계산하는 C언어 프로그램입니다.',
    '17': '단일 연결 리스트(Single Linked List)의 노드 포인터 연결을 반대로 뒤집는 역순(Reverse) 알고리즘입니다.',
    '18': '단일 연결 리스트의 중간에 신규 노드를 정확한 위치에 삽입(Insertion)하는 C언어 구현 코드입니다.',
    '19': '배열(Array)을 활용하여 LIFO(후입선출) 방식의 스택 데이터 구조와 Push/Pop 연산을 구현한 코드입니다.',
    '20': '스택(Stack) 자료구조를 활용하여 수식을 후위 표기법(Postfix)으로 변환하고 계산하는 사칙연산 프로그램입니다.',
    '21': '배열 기반 스택 포인터의 위치를 제어하며 데이터를 입출력하는 2차 스택 구현 노트입니다.',
    '22': 'FIFO(선입선출) 구조의 큐(Queue)를 배열로 구현하여 Enqueue 및 Dequeue 연산을 처리하는 프로그램입니다.',
    '23': '이진 트리를 너비 우선 탐색(BFS) 방식으로 방문하는 Level-Order 레벨 순회 출력 알고리즘입니다.',
    '24': '동적 배열의 메모리를 0으로 초기화하는 memset() 및 문자열을 안전하게 복사하는 strcpy() 함수 활용법입니다.',
    '25': '인접한 두 원소를 비교하며 순차적으로 정렬하는 버블 정렬(Bubble Sort) 알고리즘 구현 코드입니다.',
    '26': 'C언어에서 함수 주소를 포인터 배열에 저장하여 사칙연산을 동적으로 호출하는 함수 포인터 활용법입니다.',
    '27': 'malloc() 동적 메모리 할당을 통해 2차원 이중 동적 배열을 생성하고 반환하는 C언어 예제입니다.',
    '28': '각 행마다 가변적인 열 크기를 갖는 가변 2차원 동적 배열 메모리 할당 및 출력 방법입니다.',
    '29': 'C언어 clock() 함수를 활용하여 특정 알고리즘이나 코드 블록의 실행 시간을 초 단위로 측정하는 방법입니다.',
    '30': '동적 할당된 노드의 연결을 먼저 끊은 후 free() 함수를 호출하여 메모리 누수를 방지하는 노드 삭제 기법입니다.',
    '31': '사용자 입력 문자열을 순회하며 소수점과 숫자 범위를 판별하는 C++ 문자열 숫자 검증 함수입니다.',
    '32': 'C++ cin 입력 스트림에서 잘못된 문자가 입력되었을 때 무한 루프에 빠지는 현상을 해결하는 예외 처리 코드입니다.',
    '33': '안드로이드 앱에서 키-값(Key-Value) 형태로 환경 설정 데이터를 영구 저장하는 SharedPreferences 사용법입니다.',
    '34': '안드로이드 액티비티 메뉴 바에 옵션 메뉴(Option Menu)를 구성하고 클릭 이벤트를 처리하는 구현 코드입니다.',
    '35': '안드로이드 상태바 알림(Notification) 메시지를 생성하고 터치 시 액티비티로 이동시키는 방법입니다.',
    '36': '구글 GCM(Google Cloud Messaging) 푸시 서버와 연동하여 안드로이드 앱으로 푸시 알림을 발송하는 절차입니다.',
    '37': '안드로이드 외부 저장소(SD 카드) 경로를 조회하고 파티션에 파일 읽기/쓰기를 수행하는 코드입니다.',
    '38': '안드로이드 UI 버튼의 클릭 이벤트를 콜백(Callback) 인터페이스 방식으로 리스너에 등록하는 방법입니다.',
    '39': '이클립스 안드로이드 개발 환경에서 XML 레이아웃 수정 시 자동 컴파일(Auto Launch)을 설정하는 방법입니다.',
    '40': '안드로이드 스마트폰에 우분투(Ubuntu) 리눅스 환경을 커스텀 설치하고 쉘에 접속하는 구축 절차입니다.',
    '41': 'VMware 가상 머신 상에 우분투(Ubuntu) 리눅스 OS를 설치하고 네트워크 및 기본 환경을 구축하는 노하우입니다.',
    '42': 'Oracle Database Express Edition 11g 데이터베이스 설치 및 서비스 기동 설정 노트입니다.',
    '43': 'Oracle SQL Developer 도구에서 자주 쓰는 자동 정렬, 주석, 쿼리 실행 단축키 모음입니다.',
    '44': 'Oracle PL/SQL 익명 블록 구조와 변수 선언, 조건문 및 반복문 기초 작성법입니다.',
    '45': '테이블에 INSERT/UPDATE 이벤트 발생 시 자동으로 실행되는 Oracle 데이터베이스 트리거(Trigger) 구현입니다.',
    '46': '유닉스/리눅스 환경에서 C언어 소스 코드 빌드 과정을 자동화하는 Makefile 작성 가이드입니다.',
    '47': 'IIS 7.0 웹 서버 설치 후 ASP 파일 접근 시 발생 404.3 Not Found 오류를 역할 서비스 추가로 해결하는 조치법입니다.',
    '48': 'PHP 스크립트 실행 시 $_SERVER[\'PHP_SELF\'] 구문을 활용해 현재 실행 중인 파일 경로를 알아내는 방법입니다.',
    '49': 'PHP와 MySQL 데이터베이스 연동 시 한글 깨짐을 방지하기 위한 SET NAMES UTF8 인코딩 설정법입니다.',
    '50': '자바 서버 환경에서 GCM Sender 라이브러리를 활용해 안드로이드 단말로 푸시 메시지를 발송하는 코드입니다.',
    '51': '자바 SimpleDateFormat 클래스를 사용하여 날짜 포맷을 원하는 연-월-일 시:분:초 문자열로 변환하는 방법입니다.',
    '52': '자바 소켓(Socket) 통신을 통해 클라이언트와 서버 간 바이너리 파일을 송수신하는 코드입니다.',
    '53': '이클립스(Eclipse) IDE에서 개발 눈의 피로를 줄이기 위한 컬러 테마(Color Theme) 설정 방법입니다.',
    '54': '자바 File 객체를 활용하여 여러 텍스트 파일을 하나로 병합하거나 특정 파일을 삭제하는 코드입니다.',
    '55': '자바 Timer 및 TimerTask 클래스를 활용해 일정한 시간 간격으로 백그라운드 작업을 주기적으로 실행하는 방법입니다.',
    '56': '자바 Map 콜렉션 요소를 복사하거나 병합할 때 발생할 수 있는 참조 오류 및 예외 처리 주의사항입니다.',
    '57': '엑셀 VBA(Visual Basic for Applications) 매크로 작성을 위한 개발 도구 탭 활성화 및 시작 가이드입니다.',
    '58': 'VBA 매크로를 사용하여 엑셀 워크시트 셀 데이터를 동적으로 제어하고 자동화하는 코드입니다.',
    '59': '엑셀 VBA 프로그래밍에서 사용되는 핵심 변수 선언, 조건문, 반복문 주요 문법 정리입니다.',
    '61': '완전 이진 트리 기반의 힙(Heap) 구조를 활용하여 최댓값을 추출해 정렬하는 힙 정렬(Heap Sort) 알고리즘입니다.',
    '62': '비트코인(Bitcoin) 블록체인 네트워크의 화폐 기능성과 대안 화폐로서의 가능성에 대한 토론 정리입니다.',
    '63': '웨어러블 컴퓨터(Google Glass) 출시에 따른 개인정보 보호 이슈 및 기술적 영향 토론 정리입니다.',
    '64': 'LIFO 구조의 스택(Stack)과 FIFO 구조의 큐(Queue)의 데이터 입출력 방식 차이점 비교 정리입니다.',
    '65': '객체지향 프로그래밍(OOP)의 4대 핵심 요소인 캡슐화, 상속, 다형성, 추상화 개념 정리입니다.',
    '66': '금융 보안을 위협하는 스미싱, 스머핑, IP 스푸핑, 파밍의 개념과 공격 차이점 비교입니다.',
    '68': '자바 Scanner 및 System.in 입력 스트림을 사용하여 콘솔에서 사용자 입력값을 수신하는 방법입니다.',
    '69': '자바 메서드 오버로딩(Overloading) 개념과 가변인자(Varargs)를 활용한 동적 매개변수 처리 코드입니다.',
    '70': '자바 8에 도입된 람다식(Lambda Expression)을 활용하여 익명 함수 형태로 코드를 간결하게 작성하는 가이드입니다.',
    '71': '자바 제네릭(Generic) 타입을 사용하여 클래스나 메서드의 컴파일 타임 타입 안정성을 확보하는 방법입니다.',
    '72': 'ADB Wireless 기능을 활용해 USB 케이블 연결 없이 Wi-Fi 네트워크상에서 안드로이드 앱을 디버깅하는 설정입니다.',
    '73': '노트북의 무선 랜카드를 가상 AP(핫스팟)로 구성하여 주변 기기 네트워크 접속을 공유하는 설정입니다.',
    '74': '리눅스 원격 서버에 SSH(Secure Shell)를 사용하여 보안 터미널로 접속하는 기본 커맨드입니다.',
    '75': '리눅스 콘솔 터미널 환경에서 javac / java 및 gcc 커맨드로 소스 코드를 컴파일하고 실행하는 절차입니다.',
    '76': '이클립스 IDE 사용 시 개발 속도를 올려주는 필수 단축키 및 유용한 환경 설정 팁 모음입니다.',
    '78': '자바 웹 애플리케이션 패키징 파일인 WAR(Web Application Archive)를 빌드하고 톰캣에 배포하는 방식입니다.',
    '84': 'Git 버전 관리 시스템의 핵심 커맨드인 init, commit, branch, merge, log 사용법 모음입니다.',
    '88': 'JEUS 8 WAS 서버의 노드 인스턴스 기동 및 웹 애플리케이션(.war) 디플로이 조치 안내입니다.',
    '89': '리눅스 및 윈도우 인프라 서버 운용 시 자주 사용하는 필수 시스템 제어 커맨드 모음집입니다.',
    '90': '자바(Java) 언어의 핵심 객체지향 특징, 메모리 영역(Heap/Stack) 및 기본 문법 정리입니다.',
    '91': '행위 디자인 패턴 중 객체의 알고리즘을 캡슐화하여 동적으로 교체하는 전략 패턴(Strategy Pattern) 구현입니다.',
    '93': 'macOS 환경에서 터미널 개발 환경 세팅, Homebrew 패키지 관리 및 유용한 커스텀 설정 단축키입니다.',
    '94': '최신 안드로이드 스튜디오 환경에서 과거 프로젝트 호환성을 유지하기 위한 SDK 및 Gradle 세팅입니다.',
    '96': 'React Native 개발을 위한 Node.js, Watchman, Android SDK 환경 변수 설정 절차입니다.',
    '97': 'MS SQL Server 데이터베이스에서 자주 쓰이는 핵심 DDL/DML 구문 및 시스템 테이블 조회 노하우입니다.',
    '98': 'React 프레임워크의 컴포넌트 생명주기(Lifecycle) 및 State/Props 상태 관리 기초 개념입니다.',
    '101': 'Jenkins CI/CD 파이프라인을 구축하여 파이프라인 기반 자동 빌드 및 서버 배포를 수행하는 가이드입니다.',
    '102': 'React Native 앱의 수동 스토어 업데이트 없이 자바스크립트 커밋을 즉시 배포하는 CodePush Android 적용법입니다.',
    '103': 'Windows PowerShell 스크립트를 활용해 인프라 시스템 제어 및 명령어 자동화를 수행하는 가이드입니다.',
    '104': 'React Native 기본 컴포넌트(View, Text, Image) 사용법과 스타일링(StyleSheet) 기초 가이드입니다.',
    '105': 'React Native에서 배열 데이터(Array)를 map() 함수로 순회하여 리스트 컴포넌트로 렌더링하는 법입니다.',
    '106': 'Node.js Express 프레임워크를 기반으로 RESTful 웹 서버 API를 구축하고 라우팅을 처리하는 코드입니다.',
    '108': 'Let\'s Encrypt Certbot을 사용하여 웹 서버에 무료 SSL/TLS 보안 인증서를 발급 및 자동 갱신하는 설정입니다.',
    '109': 'HTTP 통신 시 소켓 커넥션을 재사용하여 연결 지연 시간을 줄이는 HTTP Connection Pool 최적화 방법입니다.',
    '110': 'Microsoft Exchange Server와 연동하여 이메일 및 일정 데이터를 EWS API로 동기화하는 개발 노트입니다.',
    '111': '개발 생산성을 극대화하기 위한 Windows, Mac, IDE 주요 필수 단축키 정리입니다.',
    '112': '자바스크립트 비동기 처리 방식인 콜백(Callback) 함수와 네트워크 통신 처리 패턴 설명입니다.',
    '113': 'Docker 컨테이너 생성, 이미지 빌드(docker build) 및 서비스 실행(docker run) 핵심 커맨드 가이드입니다.',
    '114': 'CentOS 리눅스 서버에서 패키지 업데이트(yum), 방화벽 개방(firewalld) 및 서비스 등록 방법입니다.',
    '115': 'MySQL 데이터베이스 성능 최적화, 인덱스 생성 및 사용자 계정 권한 부여 명령어 정리입니다.',
    '117': 'Elasticsearch 분산 검색 엔진의 인덱싱 구조, 매핑 설정 및 REST API 검색 쿼리 사용법입니다.',
    '118': 'Apache JMeter 부하 테스트 도구를 사용해 웹 서버 및 API의 부하 응답 성능을 측정하는 방법입니다.',
    '119': 'Wireshark 네트워크 패킷 분석 도구를 활용해 TCP/UDP 핸드셰이크 패킷 수집 및 캡처를 분석하는 가이드입니다.',
    '120': '안드로이드 HttpURLConnection 전송 시 setDoInput 및 GET/POST 메서드 호출 순서 오류 조치법입니다.',
    '121': 'DevLion 브랜드 아이덴티티 및 백엔드 인프라 기술 블로그 운용 철학 노트입니다.',
    '122': 'Android Studio IDE에서 자주 발생하는 Gradle 빌드 렌더링 에러 및 캐시 초기화 조치 방법입니다.',
    '123': '자바 Reflection API를 활용해 런타임에 클래스 메타정보를 동적으로 조회하고 객체를 제어하는 코드입니다.',
    '124': '네트워크 포트(Port)의 기본 개념과 자주 사용되는 주요 서비스별 필수 포트 번호(22, 80, 443 등) 모음집입니다.',
    '125': 'MS SQL Server에서 데이터베이스 LOCK(블로킹) 장애 발생 시 sp_who2 및 계층 쿼리로 원인 프로세스를 추적해 해제하는 방법에 대한 노트입니다.',
    '126': 'Apache Commons Daemon(prunsrv)을 사용해 Spring Boot Executable Jar 파일을 Windows 서비스로 등록하는 절차입니다.',
    '127': 'Docker 기반의 GitLab CE 컨테이너를 구동하여 사내 독립 Git 저장소 및 SSL/메일을 세팅하는 절차입니다.',
    '128': 'Prometheus 시계열 DB와 Grafana 시각화 대시보드를 연동해 서버 및 앱 메트릭을 모니터링하는 세팅입니다.',
    '129': 'Windows 실행 창(Win + R)에서 빠르게 시스템 설정 및 서비스 관리자(services.msc)를 띄우는 단축 명령어입니다.',
    '130': 'curl 명령어로 커스텀 Host 헤더를 지정하고 HTTP GET 요청으로 헬스체크 및 도메인 라우팅을 테스트하는 방법입니다.',
    '132': 'AWS EC2 가상 서버 생성 후 SSH 접속, Nginx 웹 서버 및 Java, Tomcat 9 WAS 환경 구축 절차입니다.',
    '134': 'IntelliJ IDEA에서 개발 생산성을 올리기 위한 자동 클래스 임포트(Auto Import)와 필수 단축키 세팅 가이드입니다.'
}

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

    precise_sum = PRECISE_SUMMARIES.get(pid, f'{title_clean}의 실무 핵심 개념과 주요 커맨드를 정돈한 기술 노트입니다.')
    new_summary_box = f"> **[핵심 요약]**\n> {precise_sum}"

    # Clean existing summary box
    new_body = re.sub(r'>\s*\*\*\[핵심 요약\]\*\*\s*\n*(>[^\n]*\n*)*', '', body, flags=re.MULTILINE)
    
    # Prepend new precise summary box
    new_body = new_summary_box + "\n\n" + new_body.strip()

    # Completely wipe meta commentary strings
    new_body = new_body.replace('대학생 1학년 눈높이에 맞춰 정리한 기술 노트입니다.', '')
    new_body = new_body.replace('대학교 1학년 눈높이에 맞춰 정리한 기술 노트입니다.', '')
    new_body = new_body.replace('초보자 분들도 쉽게 이해할 수 있도록 기본 용어 개념과 배경 지식을 먼저 설명하고, 실제 적용 코드와 실행법을 차근차근 다룹니다.', '')

    # Clean double Liquid raw tags
    new_body = re.sub(r'({% raw %}\s*)+', '{% raw %}\n', new_body)
    new_body = re.sub(r'(\s*{% endraw %})+', '\n{% endraw %}', new_body)

    if '{{' in new_body or '{%' in new_body:
        if '{% raw %}' not in new_body:
            new_body = "{% raw %}\n" + new_body.strip() + "\n{% endraw %}"

    new_body = re.sub(r'\n{3,}', '\n\n', new_body)
    new_fm = yaml.dump(meta, allow_unicode=True, sort_keys=False).strip()
    new_file_content = f"---\n{new_fm}\n---\n{new_body}"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_file_content)

def main():
    updated_count = 0
    for f in sorted(os.listdir(POSTS_DIR)):
        if f.endswith('.md'):
            process_file(os.path.join(POSTS_DIR, f))
            updated_count += 1
    print(f"Successfully updated real technical core summaries across all {updated_count} posts!")

if __name__ == '__main__':
    main()
