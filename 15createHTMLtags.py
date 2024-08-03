# create HTML tags for string

def createHTMLtags(tag, init_str):
    return "<" + tag +">" + init_str + "</" + tag + ">"

print(createHTMLtags('i','Python'))
print(createHTMLtags('b','Python Tutorial'))

