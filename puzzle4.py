import os



f = open("day2input.txt")

my_dict = {}
line_count = 0
for line in f:
    line_count += 1
    key, val = line.split()
    my_dict[line_count] = [key, val]
    

print(my_dict[1][0])

aim = 0
depth = 0
position = 0
for i in my_dict.keys():
    if 'down' in my_dict[i][0]:
        #depth += int(my_dict[i][1])
        aim += int(my_dict[i][1])
    elif 'up' in my_dict[i][0]:
        #depth -= int(my_dict[i][1])
        aim -= int(my_dict[i][1])
    elif 'forward' in my_dict[i][0]:
        position += int(my_dict[i][1])
        if aim > 0:
            depth += aim * int(my_dict[i][1])

print("position: %s depth: %s" % (position, depth))
print(position * depth)