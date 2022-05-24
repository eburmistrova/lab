import json

with open("animals.json", "r") as read_file:
    data = json.load(read_file)

birds = filter(lambda d: d['animal_type'] == 'Bird', data)
print('Данные о птицах', list(birds))

diurnal = filter(lambda d: d['active_time'] == 'Diurnal', data)
print('Количество дневных животных =', len(list(diurnal)))

weight = sorted(data, key=lambda d: d['weight_min'])
print('Животное с наименьшим весом -', list(weight)[0]['name'])

# git commit