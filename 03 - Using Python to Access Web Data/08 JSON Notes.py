# Dallin Romney
# JSON Notes

import json

# JSON represents data as nested "lists" and "dictionaries"

# PART 1: Dictionary
print('Part 1:')
data1 = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''
    
info1 = json.loads(data1) # loads = load from string, returns dict!!!
print('Name:',info1["name"])
print('Hide:',info1["email"]["hide"])


# PART 2: List of Dictionaries
print('\nPart 2:')

data2 = '''
[
    { "id" : "001", 
      "x" : "2",
      "name" : "Chuck"
    } ,
    { "id" : "009", 
      "x" : "7",
      "name" : "Brent"
    }
]'''

info2 = json.loads(data2)
print('User count:', len(info2))
for item in info2:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

