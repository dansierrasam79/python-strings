# reverse words in string
init_string = "The quick brown fox jumps over the lazy doggies"
init_string_list = init_string.split(" ")
init_final_list = []
sentence = ""
for word in init_string_list:
    init_final_list.append(word[::-1])

for item in init_final_list:
    sentence += item + " "
print(sentence)
