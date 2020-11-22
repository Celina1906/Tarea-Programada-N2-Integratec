import requests

r = requests.get('https://www.tec.ac.cr/carreras')

print(type(r))

data=r.text
print(type(data))