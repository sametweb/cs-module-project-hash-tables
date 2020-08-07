import urllib.request

url = 'https://www.google.com'

cache = {}

page = None

if url in cache:
    page = cache[url]

else:
    print('getting, from server')

    response = urllib.request.urlopen(url)
    data = response.read()

    cache[url] = data

    page = cache[url]

print(page)
