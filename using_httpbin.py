import requests 

response = requests.post("https://www.httpbin.org/post", data={'ocean': 'Atlantic', 'fish': 'tuna'})

print(response.text)