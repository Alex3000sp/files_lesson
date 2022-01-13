import pickle
import pickletools
import json
import yaml
from pydantic import BaseModel
import pandas as pd
# Write ifo and read

file = open('text.txt', 'a')
file.write("Hello, Men")
file.close()
file = open('text.txt', 'r')
print(file.read())
file.close()

#Second variant

with open('text.txt') as file:
    print(file.read())
file.close()

#Pickle
class Dump:
    def func():
        print('Hi there')

with open('dump', 'wb') as file:
    pickle.dump(Dump.func, file)

with open('dump', 'rb') as file:
    g = pickle.load(file)
    print(g)

#JSON/Yaml

data = {
    'age': 45,
    'name': 'Peter',
        'children': [
        {
            'age': 3,
            'name': 'Alice'
        }
    ],
    'married': True,
    'city': None
}

#JSON

with open('json_dump', 'w') as file:
    json.dump(data, file)

with open('json_dump', 'r') as file:
    g = json.load(file)
    print(g)

#Yaml

with open('yaml_dump', 'w') as file:
    yaml.safe_dump(data, file)

with open('yaml_dump', 'r') as file:
    g = yaml.safe_load(file)
    print(g)

#Pydantic

class Human(BaseModel):
    name: str
    age: str
    children: list

print(Human(**data))

#Pandas

def xlsx_to_csv_pd():
    data_xls = pd.read_excel('table.xlsx', index_col=0)
    data_xls.to_csv('2.csv', encoding='utf-8')

xlsx_to_csv_pd()