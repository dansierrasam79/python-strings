#4copiesstring
def createfourstr(init_str):
    if len(init_str) < 2:
        return "No string"
    else:
        return init_str[-2:]*4

print(createfourstr("o"))
print(createfourstr("Python"))
