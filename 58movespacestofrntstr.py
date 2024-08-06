#move spaces to front of string
init_string = 'the quick brown fox jumps over the lazy dog'
count = 0
for char in init_string:
    if char == " ":
        count += 1
final_string = init_string.replace(" ","")
final_str_spaces = " "*count
print(final_str_spaces + final_string)
