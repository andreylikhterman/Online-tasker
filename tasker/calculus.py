with open("Задавальник-Матан.txt") as file:
    text = file.readlines()
task = {}
tasks_count = 0
table = False
for line in text:
    if line[:8] == '1 неделя':
        table = True
        tasks_count += 1
        task[str(tasks_count) + " задание"] = {}
    if 'неделя' in line and table:
        current_week = line[:8]
        task[str(tasks_count) + " задание"][current_week] = {}
    if '§' in line and table:
        paragraph = line[line.find('§') + 1:line.find(':')]
        line1 = line[line.find(':') + 1:].strip()
        if paragraph not in task[str(tasks_count) + " задание"][current_week]:
            task[str(tasks_count) + " задание"][current_week][paragraph] = list(line1[:-1].split('; '))
        else:
            task[str(tasks_count) + " задание"][current_week][paragraph] += list(line1[:-1].split('; '))
    if '+' in line:
        table = False
print(task)