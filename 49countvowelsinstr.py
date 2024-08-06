# count no of vowels
init_list = ['a','e','i','o','u']
init_string = "constantinople"
final_dict = {}
for vowel in init_list:
    final_dict[vowel] = init_string.count(vowel)
print(final_dict)
