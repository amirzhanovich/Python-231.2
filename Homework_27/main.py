import asyncio
import aiohttp
import os
import json
import requests
async def fetch(session, url):
    async with session.get(url) as response:
        return response.url

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        texts = await asyncio.gather(*[fetch(session, url) for url in urls])
        return texts

lst = ['https://jsonplaceholder.typicode.com/users',
       'https://jsonplaceholder.typicode.com/posts',
       'https://jsonplaceholder.typicode.com/albums']

urls = asyncio.run(fetch_all(lst))

os.mkdir(r'C:\Users\uamir\PycharmProjects\HW_27_18092023\jsonplaceholder')
os.chdir(r'C:\Users\uamir\PycharmProjects\HW_27_18092023\jsonplaceholder')

i = 1
for url in urls:
    with open(f'{i}.json', 'w') as file:
        response = requests.get(url)
        json.dump(response.json(), file, indent=2)
    i += 1

