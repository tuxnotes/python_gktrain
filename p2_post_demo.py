import requests
import json

r = requests.post('http://httpbin.org/post', data={'key': 'value'})
r.json()

python_string = {
    'key': 'value',
    'key1': 'value1',
    'key2': 'value2'
}

json_string = json.dumps(python_string)
python_string2 = json.loads(json_string)
