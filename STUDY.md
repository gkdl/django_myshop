# 🧩 Django 세션(Session)
:contentReference[oaicite:0]{index=0}는 익명 세션과 인증된 사용자 세션을 모두 지원하는 세션 프레임워크를 제공한다.

- 각 방문자별 데이터를 서버 측에 저장할 수 있다.
- 세션 데이터는 서버에 저장되며, 쿠키 기반 세션 엔진을 사용하지 않는 한 쿠키에는 세션 ID만 저장된다.
- 세션을 사용하려면 `SessionMiddleware`가 활성화되어 있어야 한다.

```python
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
]
```

# 기본 세션 사용법
request.session['foo'] = 'bar'   # 세션 값 설정
request.session.get('foo')       # 세션 값 조회
del request.session['foo']       # 세션 값 삭제

# 세션 저장 방식 (Session Backends)
| 저장 방식      | 설명                             |
| ---------- |--------------------------------|
| 데이터베이스 세션  | 기본 방식, 세션 데이터를 DB에 저장          |
| 파일 기반 세션   | 파일 시스템에 세션 저장                  |
| 캐시 기반 세션   | 캐시 백엔드(Redis, Memcached 등)에 저장 |
| 캐시 + DB 세션 | 캐시에 우선 저장하고 DB를 백업으로 사용 , 데이터가 아직 캐시에 없는 경우에만 데이터베이스에서 읽는다     |
| 쿠키 기반 세션   | 세션 데이터를 브라우저 쿠키에 직접 저장         |


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

# 국제화
- USE-I18N: 장고의 번역 시스템 활성화 여부를 지정하는 부울이다. 기본 값은 True이다
- USE-L10N: 지역화된 서식 지정의 활성화 여부를 나타내는 부울이다. 활성화되면 날짜 및 숫자에 지역화된 서식이 사용된다. 기본 값은 False이다.
- USE-TZ: 날짜/시간을 표준 시간대로 인식할지를 지정하는 부울이다. startproject 명령으로 프로젝트를 만들면 이 값은 True로 설정된다.
- LANGUAGE-CODE: 프로젝트의 기본 언어 코드이다. 표준 언어 ID형식이다. 지정하려면 USE-I18N이 True로 설정되어 있어야 한다.
- LANGUAGES: 프로젝트에 사용 가능한 언어가 포함된 튜플이다. 언어 코드와 언어 이름의 두 가지 튜플로 구성된다.
- LOCALE-PATHS: 장고가 프로젝트의 번역이 포함된 메시지 파일을 찾는 디렉토리의 목록이다.
- TIME-ZONE: 프로젝트의 표준 시간대를 나타내는 문자열이다. startproject 명령으로 프로젝트를 만들면 이 값은 'UTC'로 설정된다.

# 국제화 관리 명령
- makemessages: 이 명령은 소스 트리를 실행하여 번역용으로 표시된 모든 문자열을 찾고 locale 디렉터리에 .po 메시지 파일을 생성하거나 업데이트한다. 각 언어마다 단일 .po 파일이 생성된다.
- compilemessages: 기존 .po 메시지 파일을 번역을 검색하는 데 사용되는 .mo 파일로 컴파일한다.

# 장고가 현재 언어를 결정하는 방법
1. i18n_patterns를 사용하는 경우, 다시 말해 번역된 URL 패턴을 사용하는 경우에는 요청된 URL에서 언어 접두사를 찾아 현재 언어를 결정한다.
2. 언어 접두사를 찾을 수 없으면 현재 사용자의 세션에서 기존 LANGUAGE_SESSION_KEY를 찾는다.
3. 세션에 언어가 설정되어 있지 않은 경우, 현재 언어를 나타내는 쿠키를 찾는다. 이 쿠키의 이름은 LANGUAGE_COOKIE_NAME 설정에서 제공할 수 있다. 기본적으로 이 쿠키의 이름은 django_language이다.
4. 쿠키를 찾을 수 없으면 요청이 Accept-Language HTTP 헤더를 찾는다.
5. Accept-Language 헤더에 언어가 지정되지 않은 경우, 장고는 LANGUAGE_CODE 설정에 정의된 언어를 사용한다.

* 기본적으로 장고는 LocaleMiddleware를 사용하지 않는 한 LANGUAGE_CODE 설정에 정의된 언어를 사용한다.

### 장고는 템플릿의 문자열을 번역하기 위해 {% trans %} 및 {% blocktrans %} 템플릿 태그를 제공한다. 번역 템플릿 태그를 사용하려면 템플릿 상단에 {% load i18n %} 을 추가해서 템플릿을 로드해야 한다.
- {% trans %} : 번역할 리터럴을 표시할 수 있다. 내부적으로 장고는 주어진 텍스트에 gettext()를 실행한다. 단순한 번역 문자열에는 유용하지만 변수가 포함된 번역 콘텐츠는 처리할 수 없다.
- {% blocktrans %} : 플레이스홀더를 사용해서 리터럴 및 변수를 포함한 콘텐츠를 표시할 수 있다.



