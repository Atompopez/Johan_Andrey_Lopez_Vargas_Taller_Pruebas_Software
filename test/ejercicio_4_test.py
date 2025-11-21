import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'main'))
from taskmanager import TaskManager

def test_task_manager_uat():
    tm = TaskManager()

    # Agregar tareas
    task = tm.add_task("Estudiar")
    assert task["title"] == "Estudiar"

    # Editar tarea
    edited = tm.edit_task(0, "Estudiar pruebas")
    assert edited["title"] == "Estudiar pruebas"

    # Eliminar
    tm.delete_task(0)
    assert len(tm.tasks) == 0
