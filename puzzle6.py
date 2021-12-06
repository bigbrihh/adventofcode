import os



f = open("day3input.txt")
content = f.read()
content_list_oxy = content.split("\n")
content_list_co2 = content.split("\n")




print(len(content_list_oxy))
for _range in range(12):
    pos1 = ""
    if len(content_list_oxy) <= 1:
        oxy_string = content_list_oxy[0]
    else:
        for i in content_list_oxy:
            pos1 += i[_range]
        print("count %s zero: %s" % (_range, pos1.count("0")))
        print("count %s one: %s" % (_range, pos1.count("1")))
        if pos1.count("0") == pos1.count("1"):
            content_list_oxy = [i for i in content_list_oxy if i[_range] == "1"]
            print("equal, default 1")       
        elif pos1.count("0") > pos1.count("1"):
            content_list_oxy = [i for i in content_list_oxy if i[_range] == "0"]
            print("more zeros")
        else:
            content_list_oxy = [i for i in content_list_oxy if i[_range] == "1"]
            print("more ones")
        print("content_list length: %s" % len(content_list_oxy))
oxy_string = content_list_oxy[0]

print(len(content_list_co2))
for _range in range(12):
    pos1 = ""
    if len(content_list_co2) <= 1:
        co2_string = content_list_co2[0]
    else:
        for i in content_list_co2:
            pos1 += i[_range]
        if pos1.count("0") == pos1.count("1"):
            print("equal, default 0")
            content_list_co2 = [i for i in content_list_co2 if i[_range] == "0"]
        elif pos1.count("0") > pos1.count("1"):
            print("less ones")
            content_list_co2 = [i for i in content_list_co2 if i[_range] == "1"]
        else:
            print("less zeros")
            content_list_co2 = [i for i in content_list_co2 if i[_range] == "0"]
        print("content_list length: %s" % len(content_list_co2))
co2_string = content_list_co2[0]

print(oxy_string)
print(co2_string)
oxy_dec = int(oxy_string, 2)
co2_dec = int(co2_string, 2)
print(oxy_dec)
print(co2_dec)
print(oxy_dec * co2_dec)



    