#find substring that contains all valies in another string
init_string = "constantinople"
init_string2 = "asi"
temp_list = []
final_string = ""

for letter in init_string2:
    for letter2 in init_string:
        if letter == letter2:
            temp_list.append(init_string.index(letter))
min_window_list = sorted(temp_list)
print(init_string[min_window_list[0]:min_window_list[-1]+1])
