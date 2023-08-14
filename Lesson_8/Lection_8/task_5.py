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

dict_to_json_text = json.dumps(my_dict)
print(f'f{type(dict_to_json_text) = }\n{dict_to_json_text = }')

dict_to_json_text = json.dumps(my_dict,ensure_ascii=False)
print(f'f{type(dict_to_json_text) = }\n{dict_to_json_text = }')
