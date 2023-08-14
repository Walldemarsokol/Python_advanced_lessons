import json

json_text = """
[
{
  "id": 2,
  "name": "Ervin Homvell",
  "username": "Antonette",
  "email": [
    "Shanna@meilissa.tv",
    "antonette@howel.com"
  ],
  "address": {
    "street": "Victor Plains",
    "suite": "Suite 879",
    "city": "Moskow",
    "zipcode": "90566-7771",
    "geo": {
      "lat": "-43.9634",
      "lng": "-34.5634"
    }
  },
  "phone": "123-232-343-45 x09342",
  "website": "anastasia.net",
  "company": {
    "name": "Deckow-Crist",
    "catchPhrase": "Proactive didactic contingency",
    "bs": "synergize scalable supply-chains"
  }
}
]
"""

print(f'{type(json_text) = }\n{json_text = }')
json_list = json.loads(json_text)
print(f'{type(json_list) = }\t{len(json_list) = }\n{json_list = }')