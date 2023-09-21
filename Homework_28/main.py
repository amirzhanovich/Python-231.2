import os
import random

import requests
import aiohttp
import asyncio

url1 = 'https://celes.club/uploads/posts/2022-11/1667313261_1-celes-club-p-oboi-na-rabochii-stol-priroda-more-krasivo-1.jpg'
url2 = 'https://celes.club/uploads/posts/2022-11/1667313268_3-celes-club-p-oboi-na-rabochii-stol-priroda-more-krasivo-3.jpg'
url3 = 'https://celes.club/uploads/posts/2022-11/1667313248_4-celes-club-p-oboi-na-rabochii-stol-priroda-more-krasivo-4.jpg'
url4 = 'https://celes.club/uploads/posts/2022-11/1667313235_5-celes-club-p-oboi-na-rabochii-stol-priroda-more-krasivo-5.jpg'
url5 = 'https://celes.club/uploads/posts/2022-11/1667313220_6-celes-club-p-oboi-na-rabochii-stol-priroda-more-krasivo-6.jpg'
url6 = 'https://celes.club/uploads/posts/2022-11/1667313216_7-celes-club-p-oboi-na-rabochii-stol-priroda-more-krasivo-7.jpg'
url7 = 'https://celes.club/uploads/posts/2022-11/1667313279_8-celes-club-p-oboi-na-rabochii-stol-priroda-more-krasivo-8.jpg'
url8 = 'https://celes.club/uploads/posts/2022-11/1667313261_9-celes-club-p-oboi-na-rabochii-stol-priroda-more-krasivo-9.jpg'
url9 = 'https://celes.club/uploads/posts/2022-11/1667313241_10-celes-club-p-oboi-na-rabochii-stol-priroda-more-krasivo-10.jpg'
url10 = 'https://celes.club/uploads/posts/2022-11/1667313248_11-celes-club-p-oboi-na-rabochii-stol-priroda-more-krasivo-12.jpg'
urls = [url1, url2, url3, url4, url5, url6, url7, url8, url9, url10]

# #решение с requests
# i = 1
# for url in urls:
#     response = requests.get(url)
#     # print(response)
#     os.mkdir(rf'C:\Users\uamir\PycharmProjects\HW_28_19092023\{i}')
#     os.chdir(rf'C:\Users\uamir\PycharmProjects\HW_28_19092023\{i}')
#     with open(f'img{i}.jpg', 'wb') as file:
#         file.write(response.content)
#     i += 1

# #решение с aiohttp
# async def func(session, url):
#     async with session.get(url) as response:
#         return response.url
# async def func_all(urls):
#     async with aiohttp.ClientSession() as session:
#         texts = await asyncio.gather(*[func(session, url) for url in urls])
#         return texts
#
# asyncio.run(func_all(urls))
#
# for url in urls:
#     x = input("Введите название папки, куда хотите сохранить файл: ")
#     os.mkdir(rf'C:\Users\uamir\PycharmProjects\HW_28_19092023\{x}')
#     os.chdir(rf'C:\Users\uamir\PycharmProjects\HW_28_19092023\{x}')
#     with open(f'img{x}.jpg', 'wb') as file:
#         response = requests.get(url)
#         file.write(response.content)