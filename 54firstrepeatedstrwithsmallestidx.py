# find repeated value with smallest index
init_string = "constantinople"
count_dict = {}
for i in range(0,len(init_string)):
    count = 0
    index_val = 0
    idx_vals = []
    for j in range(0,len(init_string)):
        if init_string[i] == init_string[j]:
            count += 1
            idx_vals.append(index_val)
        index_val += 1
    count_dict[init_string[i]] = [count, idx_vals]
repeated_dict = {}
for key,value in count_dict.items():
    if value[0] > 1:
        repeated_dict[key] = value
min_index, min_index_key = len(init_string), 0
for key,value in repeated_dict.items():
    if value[1][0] < min_index:
        min_index = value[1][0]
        min_index_key = key
print("Most repeated char: ", min_index_key)
print("With least index value: ", min_index)
