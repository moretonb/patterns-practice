from app.src.data.client import redis_client

def delete_task(id):
    task_id = f'task:{id}'

    redis_client.srem('tasks', task_id)
    redis_client.hdel(task_id, 'id', 'title', 'description')