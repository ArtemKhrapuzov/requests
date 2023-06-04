import requests

url = input()
res = []
response = requests.get(f"http://{url}/users")
data = response.json()
for i in data:
    res.append(f"{i['last_name']} {i['first_name']}")
for j in sorted(res):
    print(j)