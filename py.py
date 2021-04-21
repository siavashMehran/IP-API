import json


a = [1, 2, 3, 4, 9]
b = [12, 324, 124, 346, 5]
c = ['a', 'b', 'c', 'f', 'g']
d = {
    '1':'asd',
    'sac' : 'this somje txt', 
    '13': 3, 
    13  : 'ass', 
    'some_list' : {'key1': 'val1', 2:3}
}
dum = json.dumps(d, indent=4)

for s in d:
    key = s
    value = d[s]
    
    if type(value) != dict:
       
        print(key), print(value)
        print('\n')

    elif type(value) == dict:
        for level2value in value:
            print(level2value)
            print(value[level2value])
        
    
