from flask import Blueprint, jsonify, abort
from app.src.modules.tasks.models.task import Task
from app.src.data.tasks.queries.get_task_by_id import get_task_by_id
from app.src.data.tasks.queries.get_all_tasks import get_all_tasks

tasks_module = Blueprint('tasks', __name__, url_prefix='/tasks')

@tasks_module.route('/')
def task_list():
    db_result = get_all_tasks()
    return jsonify(tasks=[Task(int(task['id']), task['title'], task['description']).serialize() for task in db_result])

@tasks_module.route('/<int:id>')
def task_by_id(id):
    db_result = get_task_by_id(id)
    if db_result:
        task = Task(int(db_result['id']), db_result['title'], db_result['description'])
        return jsonify(task.serialize())
    return abort(404)