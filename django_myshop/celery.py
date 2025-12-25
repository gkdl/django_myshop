import os
from celery import Celery

# Celery 커맨드라인 프로그램에 대해 DJANGO_SETTINGS_MODULE 변수를 설정한다.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_myshop.settings')

# 애플리케이션 인스턴스를 생성한다.
app = Celery('django_myshop')

# 프로젝트 설정에서 커스텀 구성을 로드한다. namespace 속성은 settings.py 파일에 Celery 관련 설정이 가질 접두사를 지정한다.
# CELERY 네임스페이스를 설정하면 Celery 설정의 이름에 CELERY_접두사가 포함되어야 한다.
app.config_from_object('django.conf:settings', namespace='CELERY')

# 애플리케이션의 비동기 작업을 자동으로 검색하도록 Celery에 지시한다.
# Celery는 INSTALLED_APPS에 추가된 애플리케이션의 각 애플리케이션 디렉터리에서 tasks.py 파일을 찾은 후 이 파일에 정의된 비동기 작업을 로드한다.
app.autodiscover_tasks()
