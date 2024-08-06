#capitalize first last letters in words of a sentence
init_string = 'the quick brown fox jumps over the lazy dog'
init_list = init_string.split(" ")
final_string = ""
for item in init_list:
    final_string += item[0].upper() + item[1:-1] + item[len(item)-1].upper() + " "
print(final_string)
