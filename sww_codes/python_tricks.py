def yell(text):
    return text.upper() + '!'

bark = yell

del yell

def yell(num):
    return 1000 * num

print(yell('putin — huilo'))
print(bark('putin — huilo'))