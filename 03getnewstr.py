# create new strings
init_str = 'w'
if len(init_str) >= 2:
    final_str = init_str[:2] + init_str[-2:]
else:
    final_str = init_str
print(final_str)
