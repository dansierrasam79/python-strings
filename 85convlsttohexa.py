#convert int list to hexadecimal num
init_list = [111, 12, 45, 67, 109]
second_list,final_list = [],[]
final_string = ""

for num in init_list:
    second_list.append(hex(num))

for hexa in second_list:
    if len(hexa) == 4:
        final_string += hexa[2:len(hexa)]
    else:
        final_string += hexa[0] + hexa[-1]
print(final_string)
