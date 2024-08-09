#compute sum of two nums
init_str_tup = ("1000","10")
total = 0
try:
    total = int(init_str_tup[0]) + int(init_str_tup[1])
    print(str(total))
except:
    print("One of the operands is not an integer")
