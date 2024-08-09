#find smallest largest word in str
init_string = 'the quickest brown fox jumps over the lazy dog'
init_list = init_string.split(" ")
init_dict,ordered_dict = {},{}
for item in init_list:
    init_dict[item] = len(item)
ordered_tuplist = sorted(init_dict.items(),key=lambda item:item[1])
print(ordered_tuplist[0],ordered_tuplist[-1])
