# 장고 세션
- 장고는 익명 세션과 사용자 세션을 지원하는 세션 프레임워크를 제공한다.
- 세션 프레임워크를 사용하면 각 방문자의 데이터를 저장할 수 있다.
- 세션 데이터는 서버 측에 저장되며, 쿠키 기반 세션 엔진을 사용하지 않는 한 쿠키에는 세션 ID를 담는다.
- 세션을 사용하려면 프로젝트의 MIDDLEWARE 설정에 django.contrib.sessions.middleware.SessionMiddleware 가 포함되어 있는지 확인해야 한다.


1. request.session['foo'] = 'bar' - 세션에서 변수 설정
2. request.session.get('foo')     - 세션 키를 조회
3. del request.session['foo']     - 이전에 세션에 저장한 키를 삭제

### 장고는 세션 데이터 저장을 위해 다음과 같은 옵션을 제공한다.
- 데이터베이스 세션: 세션 데이터가 데이터베이스에 저장된다. 기본 세션 엔진이다.
- 파일 기반 세션: 세션 데이터가 파일 시스템에 저장된다.
- 캐시 기반 세션: 세션 데이터는 캐시 백엔드에 저장된다. 캐시 설정을 사용해 캐시 백엔드를 지정할 수 있다.
- 캐시 데이터베이스 세션: 세션 데이터는 쓰기 전용 캐시와 데이터베이스에 저장된다. 데이터가 아직 캐시에 없는 경우에만 데이터베이스에서 읽는다.
- 쿠키 기반 세션: 세션 데이터는 브라우저로 전송되는 쿠키에 저장된다.

### 설정을 통해 세션을 커스터마이징할 수 있다.
- SESSION_COOKIE_AGE: 세션 쿠키의 유효 기간 이다. 기본 값은 1209600(2주)이다
- SESSION_COOKIE_DOMAIN: 세션 쿠키에 사용되는 도메인이다. 크로스 도메인 쿠키를 사용하려면 mydomain.com으로 설정하고, 표준 도메인 쿠키를 사용하려면 None으로 설정한다.
- SESSION_COOKIE_HTTPONLY: 세션 쿠키 HttpOnly 플래그에 사용여부를 지정하는 옵션이다. 이 옵션을 TRUE로 설정하면 클라이언트 측의 JavaScript에서 세션 쿠키에 액세스할 수 없다. 기본 값은 사용자 세션 하이재킹에 대한 보안을 강화하기 위해 True이다.
- SESSION_COOKIE_SECURE: HTTPS 연결인 경우에만 쿠키를 전송해야 함을 나타내는 부울 값이다. 기본 값은 False이다.
- SESSION_EXPIRE_AT_BROWSER_CLOSE: 브라우저를 닫을 때 세션을 만료해야 함을 나타내는 부울 값이다. 기본 값은 False이다.
- SESSION SAVE_EVERY_REQUEST: True인 경우 요청할 때마다 세션을 데이터베이스에 저장하는 부울 값이다. 세션이 저장될 때마다 세션 만료시점도 업데이트된다. 기본 값은 False이다.

# 세션 만료
- SESSION_EXPIRE_AT_BROWSER_CLOSE 설정을 사용해서 브라우저 기간세션 혹은 영구 세션을 사용하도록 할 수 있다.
- 이 설정은 기본적으로 False로 설정되어 세션 지속기간을 SESSION_COOKIE_AGE 설정에 저장된 값으로 강제 설정한다.
- SESSION_EXPIRE_AT_BROWSER_CLOSE를 True로 설정하면 사용자가 브라우저를 닫을 때 세션이 만료되며 SESSION_COOKIE_AGE 설정은 무시된다.
- request.session의 set_expiry() 메서드를 사용해서 현재 세션의 기간을 덮어쓸 수 있다.

# 콘텍스트 프로세서
- 콘텍스트 프로세서는 요청 객체를 인수로 받아서 요청 콘텍스트에 추가된 딕셔너리를 반환 하는 파이썬 함수이다.
- 콘텍스트 프로세서는 모든 템플릿에서 전역적으로 사용할 수 있는 함술르 만들어야 할 때 유용하다.
- django.template.context_processors.debug: 요청에서 실행된 SQL 쿼리 목록을 출력하는 콘텍스트의 debug와 sql_queries 변수를 설정한다.
- django.template.context_processors.request: 콘텍스트의 request 변수를 설정한다.
- django.contrib.auth.context_processors.auth: 요청의 user 변수를 설정한다.
- django.contrib.messages.context_processors.messages: 콘텍스트에 메시지 프레임워크를 사용해서 생성된 모든 메시지를 담는 message 변수를 설정한다.
* 또한 장고는 django.template.context_processors.csrf를 활성화해서 사이트 간 요청위조(CSRF) 공격을 방지한다.



### Celery 및 RabbitMQ와 함께 장고 사용하기
- Celery는 방대한 양의 메시지를 처리할 수 있는 분산 작업 큐이다. Celery를 사용해서 비동기 작업을 장고 애플리케이션 내에 파이썬 함수로 정의한다.