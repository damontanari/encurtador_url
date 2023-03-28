import requests, json

site_ecurtado = requests.get("http://127.0.0.1:5000/encurtar")
novo_url = site_ecurtado.json()
print(novo_url)