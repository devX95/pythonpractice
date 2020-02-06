data = {'k1': 100, 'k2': [0, 1, 2], 'k3': {'d1': 'asd'}}
print(data)

print(data['k1'])
print(data['k2'])
print(data['k2'][1])
print(data['k3']['d1'])
print(data['k3']['d1'][1])
print(data['k3']['d1'][1].upper())
print(data.keys())
print(data.values())
print(data.items())