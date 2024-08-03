# change letter to $
init_str = "google"
first_letter = init_str[0]
final_str = first_letter
for letter in init_str[1:]:
    if letter == first_letter:
        final_str += '$'
    else:
        final_str += letter
print(final_str)
