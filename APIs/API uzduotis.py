import requests

url = 'https://api.chucknorris.io/jokes/random?category={category}'
response = requests.get(url)
data = response.json()
joke = data['']
print(joke)
# traukiam kategorijas is https://api.chucknorris.io/jokes/categories
#