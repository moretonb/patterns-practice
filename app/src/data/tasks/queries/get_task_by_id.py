from app.src.data.client import redis_client

def get_task_by_id(id=0):
    return redis_client.hgetall(f'task:{id}')