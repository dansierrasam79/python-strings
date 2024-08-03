# display strings sorted
init_string = "red,white,black,red,green,black"
init_list = init_string.split(",")
final_string = ""
final_list = sorted(init_list)
for i in range(0, len(final_list)):
    final_string += final_list[i] + ","
print(final_string)
