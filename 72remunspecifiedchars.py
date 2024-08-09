# remove all chars except specified
init_string = "constantinople"
spc_char = "t"
final_string = ""
for letter in init_string:
    if letter == spc_char:
        final_string += letter
print(final_string)
