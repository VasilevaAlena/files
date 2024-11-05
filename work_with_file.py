import shutil

number_line = {}
list_line = []

with open ('1.txt', encoding='utf8') as file:
    lines_1 = 0
    for line in file:
        lines_1 += 1
        number_line['1.txt'] = lines_1
    list_line.append(lines_1)

with open ('2.txt', encoding='utf8') as file:
    lines_2 = 0
    for line in file:
        lines_2 += 1
        number_line['2.txt'] = lines_2
    list_line.append(lines_2)

with open ('3.txt', encoding='utf8') as file:
    lines_3 = 0
    for line in file:
        lines_3 += 1
        number_line['3.txt'] = lines_3
    list_line.append(lines_3)

list_line.sort()

for i in list_line:
    for k, v in number_line.items():
        if i == v:
            with open (k, 'r', encoding='utf8') as f:
                with open ('4.txt', 'a', encoding='utf8') as file:
                    file.write(f'{k}\n{v}\n')
                    shutil.copyfileobj(f, file)
                    file.write(f'\n')




