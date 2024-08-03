# return first three chars
def return_first_three(init_str):
    if len(init_str) < 3:
        return init_str
    else:
        return init_str[:3]

print(return_first_three("Python"))
print(return_first_three("py"))
