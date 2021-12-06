import os



f = open("day3input.txt")
content = f.read()
content_list = content.split("\n")


count_1 = 0
count_0 = 0
gamma_string = ""
epsilon_string = ""

pos1 = ""
pos2 = ""
pos3 = ""
pos4 = ""
pos5 = ""
pos6 = ""
pos7 = ""
pos8 = ""
pos9 = ""
pos10 = ""
pos11 = ""
pos12 = ""


for binary_string in content_list:
    pos1 += binary_string[0]
    pos2 += binary_string[1]
    pos3 += binary_string[2]
    pos4 += binary_string[3]
    pos5 += binary_string[4]
    pos6 += binary_string[5]
    pos7 += binary_string[6]
    pos8 += binary_string[7]
    pos9 += binary_string[8]
    pos10 += binary_string[9]
    pos11 += binary_string[10]
    pos12 += binary_string[11]

p_list = [pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12]

for i in p_list:
    count_0 = i.count("0")
    count_1 = i.count("1")
    print("%s : %s : %s" % (i, count_0, count_1))
    if count_0 > count_1:
        gamma_string += "0"
        epsilon_string += "1"
    else:
        gamma_string += "1"
        epsilon_string += "0"

gamma_dec = int(gamma_string, 2)
epsilon_dec = int(epsilon_string, 2)
print(gamma_dec * epsilon_dec)

    