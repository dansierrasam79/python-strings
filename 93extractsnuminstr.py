# extract numbers from string
init_string = "red 12 black 45 green"
init_list = init_string.split(' ')
final_list = []
for item in init_list:
    try:
        final_list.append(int(item))
    except:
        continue;
print(final_list)
