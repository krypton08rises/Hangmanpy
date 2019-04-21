text = 'abcdc'
result = ''
for i in text:
    if i == 'a':
        i = '\u0336'+i
    result = result + i
print(result)