import json

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

print(f'f{type(my_dict) = }\n{my_dict = }')
with open('new_user.json','w',encoding='utf-8') as f:
    json.dump(my_dict,f,ensure_ascii=False)
