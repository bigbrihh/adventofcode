import os

_file = open("puzzle1.txt", "r")
content = _file.read()
content_list = content.split("\n")
int_list = [int(x) for x in content_list]

increased = 0
decreased = 0
while len(int_list) > 3:
    x = sum(int_list[:3])
    y = sum(int_list[1:4])
    if x < y:
        increased += 1
    elif x > y:
        decreased += 1
    int_list = int_list[1:]

print(increased)
print(decreased)
