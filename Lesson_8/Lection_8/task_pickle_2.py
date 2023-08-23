import pickle
#сохранение объекта в строку байт
my_dict = {
    "firs_name":"John",
    "last_name":"Smith",
    "hobbies":["smithing","coding","travel"],
    "age":35,
    "children":[
        {
            "first_name": "Alice",
            "age":5
        },
        {
            "first_name":"Masha",
            "age":3
        }
    ]
}
print(my_dict)
res = pickle.dumps(my_dict,protocol=pickle.DEFAULT_PROTOCOL)
print(f'{res = }')
print(f'{pickle.DEFAULT_PROTOCOL = }')