import requests

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'

r = requests.get(url).text

#print(r)

letters = '!@#$%^&*()_+-={}[]?\n'

for i in letters:
    r = r.replace(i, '')

print(r)
