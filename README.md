# 🛒 Django 기반 전자상거래 프로젝트

## 📌 프로젝트 개요
본 프로젝트는 Django 기반의 웹 애플리케이션으로,  
전자상거래(쇼핑몰) 서비스에 필요한 핵심 기능들을 단계적으로 구현한 프로젝트입니다.

---

## 🔐 인증 및 세션 관리
1. Django 인증 프레임워크를 활용한 로그인 기능
2. Django 세션을 이용한 세션 설정
3. 세션 기반 쇼핑 카트 저장

---

## 🧾 주문 및 결제 시스템
4. 고객 주문 생성
5. Stripe 연동 전자결제 시스템
6. 결제 프로세스 구축
7. 웹후크(Webhook)를 사용한 결제 알림 처리

---

## 📧 비동기 처리
8. 워커, 메시지 큐, 메시지 브로커를 이용한 비동기 메일 전송

---

## 📄 데이터 출력 및 관리
9. 주문 정보 CSV, PDF 생성
10. 쿠폰 생성 및 주문에 쿠폰 적용

---

## 🤖 추천 시스템
11. Redis를 이용한 상품 추천 시스템 구축

---

## 🌍 국제화(i18n)
12. gettext, django-parler를 이용한 다국어 지원

---

## 🧰 기술 스택 (Tech Stack)

### Backend
- Python 3.x
- Django
- Django ORM

### Database
- SQLite (개발 환경 기준)
- PostgreSQL / MySQL (확장 가능 구조)

### Cache & Message Broker
- Redis

### Payment
- Stripe API

### Async / Background Task
- Celery (Worker)
- Message Queue / Broker 기반 비동기 처리

### Internationalization
- GNU gettext
- django-parler

### File & Document
- CSV 파일 생성
- PDF 문서 생성

---

## 🎯 학습 목적

본 프로젝트는 다음과 같은 학습 목표를 바탕으로 진행되었습니다.

- Django 인증 및 세션 구조에 대한 이해
- 세션 기반 상태 관리와 쇼핑 카트 구현
- 실제 결제 서비스(Stripe) 연동 경험
- 웹후크 기반 비동기 이벤트 처리
- 메시지 큐와 워커를 활용한 비동기 작업 이해
- Redis를 활용한 캐싱 및 추천 시스템 설계
- 국제화(i18n)를 고려한 서비스 설계 경험
- 실무에 가까운 전자상거래 아키텍처 학습

---