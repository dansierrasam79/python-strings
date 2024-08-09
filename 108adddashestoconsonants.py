#return dashes around consonants
vowels = ['a','e','i','o','u']
init_str = "Green"
final_str = ""
for letter in init_str:
    if letter not in vowels:
        final_str += "-" + letter + "-"
    else:
        final_str += letter
print(final_str)
