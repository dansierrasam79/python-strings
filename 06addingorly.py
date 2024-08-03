# add ing or ly
#init_str = "chase"
init_str = "chasing"

if len(init_str) >= 3:
    if init_str[-3:] == "ing":
        print(init_str+"ly")
    else:
        print(init_str + "ing")
