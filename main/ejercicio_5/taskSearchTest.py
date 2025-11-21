import time
from taskSearch import TaskSearchService

def test_search_performance():
    tasks = [{"title": f"Tarea {i}"} for i in range(1, 2000)]
    service = TaskSearchService(tasks)

    start = time.time()
    for _ in range(1000):
        service.search("100")
    end = time.time()

    assert (end - start) < 1