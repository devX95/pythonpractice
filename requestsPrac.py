import requests

response = requests.get('https://api.github.com/search/repositories', params={'q': 'requests+language:python'})

if response:
  print('Success')
  data = response.json()
  print(data['items'][0]['name'])
  print(data['items'][0]['description'])
else:
  print('Not found')
