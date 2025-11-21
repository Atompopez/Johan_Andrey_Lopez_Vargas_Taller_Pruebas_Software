import time
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'main'))
from task_search import TaskSearchService

def test_search_performance():
    tasks = [{"title": f"Tarea {i}"} for i in range(1, 2000)]
    service = TaskSearchService(tasks)

    start = time.time()
    for _ in range(1000):
        service.search("100")
    end = time.time()

    # La prueba pasa si las 1000 búsquedas tardan menos de 1 segundo
    assert (end - start) < 1

