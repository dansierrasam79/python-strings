# convert from list to str
init_list = ['Red', 100, -50, 'green', 'w,3,r', 12.12, False]
final_list = []
for item in init_list:
    final_list.append(str(item))
final_string = ''.join(final_list)
print(final_string)
