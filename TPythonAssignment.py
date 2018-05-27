
number_list = [2, 7, 12, 16, 22, 24, 30, 222]

new_number = []

for i in number_list:
    if i % 2 == 0:
        new_number.append(i)

print(new_number)