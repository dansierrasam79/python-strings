# remove punctuation from str
init_str = "String! With. Punctuation?"
punc_list = ['"',"'",'!','?','.',',']
final_str = ""
for letter in init_str:
    if letter not in punc_list:
        final_str += letter
print(final_str)
