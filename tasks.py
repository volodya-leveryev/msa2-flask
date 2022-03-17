from time import sleep
from celery import Celery
from models.solution_model import Solution

BROKER_BACKEND_URL = 'redis://localhost:6379/'

celery_app = Celery(
    __name__,
    backend=BROKER_BACKEND_URL,
    broker=BROKER_BACKEND_URL
)

@celery_app.task()
def process_solution(solution_dict):
    sol = Solution.from_dict(solution_dict)
    print(sol)
    sleep(15)  # Изображаем бурную деятельность
    return 42
