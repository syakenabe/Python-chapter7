a = [8, 19, 148, 4]
b = [9, 1, 33, 83]
new_list = []

for i, new in enumerate(a):
    num1 = a[i]
    for j,new in enumerate(b):
        num2 = b[j]
        new = num1 * num2
        new_list.append(new)

print(new_list)
