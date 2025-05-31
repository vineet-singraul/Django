import json

p_data={
    'name':True,
    'age':False,
    'quali':None,
    'active':'yes'
}
j_data=json.dumps(p_data)
print(j_data)
print(type(j_data))

j_data1='{"name": true,"age": false,"quali": null,"active": "yes"}'

p_data1=json.loads(j_data1)
print(p_data1)
print(type(p_data1))