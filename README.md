# Django 세션(Session)

Django는 익명 세션과 사용자 세션을 모두 지원하는 세션 프레임워크를 제공한다.
세션 프레임워크를 사용하면 각 방문자별 데이터를 서버 측에 저장할 수 있다.

* 세션 데이터는 서버에 저장된다.
* 쿠키 기반 세션 엔진을 사용하지 않는 한 쿠키에는 세션 ID만 저장된다.
* 세션을 사용하려면 `django.contrib.sessions.middleware.SessionMiddleware`가 활성화되어 있어야 한다.

---

## 세션 미들웨어 설정

```python
MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
]
```

---

## 세션 기본 사용법

```python
# 세션 값 저장
request.session["foo"] = "bar"

# 세션 값 조회
request.session.get("foo")

# 세션 값 삭제
del request.session["foo"]
```

---

## 세션 저장 방식(Session Engines)

Django는 세션 데이터를 저장하기 위해 다음과 같은 옵션을 제공한다.

### 데이터베이스 세션 (기본값)

* 세션 데이터가 데이터베이스에 저장된다.

### 파일 기반 세션

* 세션 데이터가 파일 시스템에 저장된다.

### 캐시 기반 세션

* 세션 데이터가 캐시 백엔드에 저장된다.
* 캐시 설정을 통해 백엔드를 지정할 수 있다.

### 캐시 + 데이터베이스 세션

* 세션 데이터는 캐시에 우선 저장된다.
* 캐시에 데이터가 없을 경우 데이터베이스에서 조회한다.

### 쿠키 기반 세션

* 세션 데이터가 암호화되어 브라우저 쿠키에 저장된다.

---

## 세션 관련 주요 설정

```python
SESSION_COOKIE_AGE = 1209600  # 기본값: 2주 (초 단위)
```

| 설정 항목                           | 설명                                   |
| ------------------------------- | ------------------------------------ |
| SESSION_COOKIE_AGE              | 세션 쿠키의 유효 기간                         |
| SESSION_COOKIE_DOMAIN           | 세션 쿠키가 적용될 도메인                       |
| SESSION_COOKIE_HTTPONLY         | JavaScript에서 쿠키 접근 차단 여부 (기본값: True) |
| SESSION_COOKIE_SECURE           | HTTPS 연결에서만 쿠키 전송 여부                 |
| SESSION_EXPIRE_AT_BROWSER_CLOSE | 브라우저 종료 시 세션 만료 여부                   |
| SESSION_SAVE_EVERY_REQUEST      | 요청마다 세션 저장 여부                        |

---

## 세션 만료(Session Expiry)

* 기본적으로 세션은 `SESSION_COOKIE_AGE` 값에 따라 유지된다.
* 브라우저 종료 시 세션을 만료하려면 다음 설정을 사용한다.

```python
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
```

### 세션별 만료 시간 설정

```python
# 현재 세션의 만료 시간 설정
request.session.set_expiry(3600)  # 1시간
```

* `0` : 브라우저 종료 시 만료
* 정수 : 초 단위
* `None` : 전역 설정값 사용

---

# 컨텍스트 프로세서(Context Processor)

컨텍스트 프로세서는 요청 객체를 인자로 받아
템플릿에서 전역적으로 사용할 수 있는 딕셔너리를 반환하는 함수이다.

모든 템플릿에서 공통으로 사용해야 하는 값이 있을 때 유용하다.

---

## 기본 제공 컨텍스트 프로세서

* `django.template.context_processors.debug`

  * debug, sql_queries 변수 제공

* `django.template.context_processors.request`

  * request 객체 제공

* `django.contrib.auth.context_processors.auth`

  * user 객체 제공

* `django.contrib.messages.context_processors.messages`

  * 메시지 프레임워크 변수 제공

* `django.template.context_processors.csrf`

  * CSRF 공격 방지를 위한 토큰 자동 주입

---

# 인증(Authentication)과 세션의 관계

Django의 인증 시스템은 세션 프레임워크를 기반으로 동작한다.

* 로그인 성공 시 사용자 ID가 세션에 저장된다.
* 이후 요청에서는 세션을 통해 현재 인증된 사용자를 식별한다.
* `request.user` 객체는 세션 정보를 기반으로 자동 설정된다.

```python
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    return HttpResponse(request.user.username)
```

---

# 세션 보안 관련 설정 팁

실무 환경에서는 세션 보안 설정이 매우 중요하다.

```python
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = "Lax"
```

* `HTTPONLY` : JavaScript를 통한 세션 탈취 방지
* `SECURE` : HTTPS 환경에서만 쿠키 전송
* `SAMESITE` : CSRF 공격 완화

---

# 세션 엔진 설정 예제

## 데이터베이스 세션 (기본)

```python
SESSION_ENGINE = "django.contrib.sessions.backends.db"
```

## 캐시 기반 세션 (Redis 예시)

```python
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
```

## 캐시 + DB 세션

```python
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
```

## 쿠키 기반 세션

```python
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
```

---

# 세션 관련 자주 발생하는 이슈

### 1. 세션이 저장되지 않는 경우

* `SessionMiddleware` 누락 여부 확인
* 응답 전에 세션 값이 변경되었는지 확인

### 2. 로그인 후 다시 익명 사용자로 처리되는 경우

* 쿠키 도메인/경로 설정 확인
* 프록시 또는 로드밸런서 환경에서 HTTPS 설정 확인

### 3. 서버 재시작 시 세션이 초기화되는 경우

* 캐시 기반 세션 사용 시 영속 캐시 여부 확인

---

# Celery 및 RabbitMQ와 Django

Celery는 Django와 함께 사용되는 대표적인 비동기 작업 큐이다.

* 웹 요청과 분리된 작업 처리 가능
* 장시간 실행 작업을 백그라운드에서 처리
* 메시지 브로커로 RabbitMQ 또는 Redis를 사용

```python
# tasks.py
from celery import shared_task

@shared_task
def send_email_task(user_id):
    pass
```

Celery를 활용하면 다음과 같은 작업을 효율적으로 처리할 수 있다.

* 이메일 및 알림 발송
* 대량 데이터 처리
* 외부 API 호출
* 배치 작업 및 스케줄링
