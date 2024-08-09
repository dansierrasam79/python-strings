# find common substring in two strings
init_string = "Python3"
init_string2 = "Python2.7"
substr_dict,final_dict = {},{}
compare_str = ""
for i in range(0,len(init_string)):
    compare_str = init_string[:i]
    if compare_str in init_string2:
        substr_dict[compare_str] = len(compare_str)
max_val = max(substr_dict.values())

for key,value in substr_dict.items():
    if value == max_val:
        print("Largest substring in second string: ", key)
        break;
