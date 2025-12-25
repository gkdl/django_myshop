# Celery 모듈을 임포트해서 장고가 시작될 때 로드되도록 해야 한다.
from .celery import app as celery_app

__all__ = ['celery_app']
