import requests
import re
payload = {'sede': 'San Carlos'}
r = requests.get('https://www.tec.ac.cr/carreras')
contenido = r.text
stripped = re.sub('<[^<]+?>', '',contenido)
print(stripped)
