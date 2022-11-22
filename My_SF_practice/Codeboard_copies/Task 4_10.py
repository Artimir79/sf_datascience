# Пример:

# tasks = [(36871, 'office', False),
# (40690, 'office', False),
# (35364, 'voltage', False),
# (41667, 'voltage', True),
# (33850, 'office', False)]
 
# print(task_manager(tasks))
# defaultdict(, {'voltage': deque([41667, 35364]),
# 'office': deque([36871, 40690, 33850])})
tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]
 
from collections import defaultdict
from collections import deque

def task_manager(tasks):
    task_dict = defaultdict(deque)
   # dq = deque()
    for task, serv, prior in tasks:
        if prior == True:
            task_dict[serv].appendleft(task)
        else:
            task_dict[serv].append(task)
    return task_dict


print(task_manager(tasks))
