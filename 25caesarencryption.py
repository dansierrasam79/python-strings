# caesar encryption
init_string = "constantinople"
temp_string = ""
final_string = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in init_string:
    temp_string = alphabet[alphabet.index(letter):] + alphabet[:alphabet.index(letter)]
    final_string += temp_string[5]
print(final_string)
