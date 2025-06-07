import json

p_data = {
    'name':True,
    'age':False,
    'quali':None,
    'active':'yas'
}

json_data = json.dumps(p_data)
print(json_data)
print(type(json_data))

json_data1 = '{"name": true, "age": false, "quali": null, "active": "yas"}'

python_data = json.loads(json_data1)
print(python_data)     
print(type(python_data))

