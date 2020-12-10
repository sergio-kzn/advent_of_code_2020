"""
"""

import data

raw_data = data.get('https://adventofcode.com/2020/day/10/input')
raw_data.remove('')

# raw_data = ['16', '10', '15', '5', '1', '11', '7', '19', '6', '12', '4', ]

current = 0
length_1 = []
length_2 = []
length_3 = []
new_data = []

raw_data.sort(key=int)

# def check(i, data, current):
#     if data == current + i:
#         new_data.append(data)
#         name = f'length_{i}'
#         globals()[name].append(data)

for i in range(len(raw_data)):

    for data in raw_data:
        data = int(data)
        if data == current+1:
            current = data
            new_data.append(data)
            length_2.append(data)
            break
        elif data == current+2:
            current = data
            new_data.append(data)
            length_2.append(data)
            break
        elif data == current+3:
            current = data
            new_data.append(data)
            length_3.append(data)
            break

my_adapter = max(raw_data, key=int)
length_3.append(int(my_adapter) + 3)


print("length_1", len(length_1))
print("length_3", len(length_3))
print("result", len(length_1) * len(length_3))










##################################
#             part 2             #
##################################
