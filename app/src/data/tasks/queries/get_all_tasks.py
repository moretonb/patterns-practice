from app.src.data.client import redis_client

def get_all_tasks():
    keys = redis_client.smembers('tasks')
    tasks = []
    for key in keys:
        db_result = redis_client.hgetall(key)
        tasks.append(db_result)

    return tasks