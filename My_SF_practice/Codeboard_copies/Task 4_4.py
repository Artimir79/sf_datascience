from hidden import north, center, south
# Пишите здесь команды, которые помогут
# найти ответы на вопросы

from collections import Counter

new_north = []
for check in north:
    for item in check:
        new_north.append(item)
new_center = []
for check in center:
    for item in check:
        new_center.append(item) 
new_south = []
for check in south:
    for item in check:
        new_south.append(item)

north_count = Counter(new_north)
print(north_count)

center_count = Counter(new_center)
print(center_count)

south_count = Counter(new_south)
print(south_count)