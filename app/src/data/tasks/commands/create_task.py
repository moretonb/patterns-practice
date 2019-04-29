from app.src.data.client import redis_client

def create_task(title, description):
    id = redis_client.incr('current_task')

    task_to_persist = {'id' : id, 'title' : title, 'description' : description }
    task_id = f'task:{id}'

    redis_client.hmset(task_id, task_to_persist)
    redis_client.sadd('tasks', task_id)

    return task_to_persist