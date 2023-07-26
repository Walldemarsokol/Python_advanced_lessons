"""генерация словарей"""

my_dictcomp = {key: chr(key) for key in range(97,123)}
print(my_dictcomp)
for number,char in my_dictcomp.items():
    print(f'{number} => {char}')