# insert str in middle of another str
def insmid(init_str, init_str2):
    final_str = init_str[:int(len(init_str)/2)] + init_str2 + init_str[int(len(init_str)/2):]
    return final_str

print(insmid('[[]]', 'Python'))
print(insmid('{{}}', 'PHP'))
