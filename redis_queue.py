import redis

r = redis.Redis(
    host = 'localhost',
    port = 6397,
    db = 0
)

# ## lists in Redis

# r.lpush("task_queue", "task1")


# #(head - left of the list)

# r.rpush("task_queue", "task2")
# r.rpush("task_queue", "task3")

# # rpush- tail of the list

# task = r.lpop("task_queue")
# print(task)
# #pop (remove and return the head)

# #rpop removes and returns the last element of the tail



def enqueue_task(queue_name, task):
    """
    appends a task to the end (right) of the redis list name queue_name"""
    r.rpush(queue_name, task)

def dequeue_task(queue_name, task):
    """removes a task from the front(left) of the queue name"""
    task = r.lpop(queue_name)
    return task.decode('utf-8') if task else None

# example usage

enqueue_task("my_queue", "send_email")
enqueue_task("my_queue", "generate_report")

while True:
    task = dequeue_task("my_queue")
    if not task:
        print("empty queue")
        break
    else:
        print("processing task")