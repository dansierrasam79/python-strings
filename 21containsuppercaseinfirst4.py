# contains two uppercase chars in first 4
init_string = "COnstantinople"
init_string2 = "constantinople"

def cnvupper(init_str):
    count = 0
    for i in range(0,4):
        if init_str[i].isupper():
            count +=1
    if count >= 2:
        return init_str.upper()
    else:
        return init_str

print(cnvupper(init_string))
print(cnvupper(init_string2))
