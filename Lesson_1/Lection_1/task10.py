LIMIT = 120
ATTENTION = 'Attention!'
name = input('Your name: ')
age = int(input('Your age: '))
text = ATTENTION + " Хоть тебе и осталось " + str(100 - age) +\
     " до ста лет, но длинна строки не должна ревышать " + str(LIMIT) + " символов."
print(text)