import requests

r = requests.get("http://api.github.com/repos/dward2/BME547/branches")
print(r)
print(type(r))
print(r.status_code)
print(r.text)
branches = r.json()
for branch in branches:
    print(branch["name"])