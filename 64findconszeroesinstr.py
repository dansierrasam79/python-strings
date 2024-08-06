#find consecutive zeroes in a string
init_string = "100111100010010"+"1"
final_string = ""
final_list = []
for i in range(0, len(init_string)):
    if init_string[i] == "0":
        final_string += "0"
    elif init_string[i] == "0" and init_string[i] == init_string[i-1]:
        final_string += "0"
    else:
        final_list.append(len(final_string))
        final_string = ""
        
print("Max consecutive zeroes: ", max(final_list))
