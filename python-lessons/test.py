import requests
import json

response = requests.get("https://api.github.com/users/octocat")
data = response.json()
with open("test.json", "w") as file:
    json.dump(data, file, indent=4)