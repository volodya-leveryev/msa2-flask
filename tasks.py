from time import sleep
from celery import Celery

BROKER_BACKEND_URL = 'redis://localhost:6379/0'

celery_app = Celery(
    __name__,
    backend=BROKER_BACKEND_URL,
    broker=BROKER_BACKEND_URL
)

@celery_app.task()
def process_solution(solution):
    print(solution.__dict__)
    sleep(30)  # Изображаем бурную деятельность
    return {}
