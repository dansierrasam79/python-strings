# gen strings with unique and duplicate chars
from collections import Counter as cnt
init_string = 'thequickbrownfoxjumpsoverthelazydog'
final_str, final_str2 = "",""
count_chars = dict(cnt(init_string))
for key,value in count_chars.items():
    if value == 1:
        final_str += key
    else:
        final_str2 += key
print(final_str)
print(final_str2)
