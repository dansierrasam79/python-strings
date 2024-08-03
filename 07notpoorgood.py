# replace not poor good
init_str = 'The lyrics is poor not!'
final_str = 'The lyrics is '
if 'not' in init_str and 'poor' in init_str:
    if init_str.index('not') > init_str.index('poor'):
        final_str += 'good'
    else:
        final_str += 'not that poor'
print(final_str)
