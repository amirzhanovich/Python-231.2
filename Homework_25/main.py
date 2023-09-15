# #practice_a&b
# from random import randint
# from time import time, sleep
# import asyncio
#
# for i in range(1,6):
#     with open(f'file{i}.txt', 'w') as file:
#         file.write(str(randint(-10, 10)))
#
# def funcRead1():
#     with open('file1.txt', 'r') as file:
#         result = file.readlines()
#         sleep(1)
#         print(result)
#
# def funcRead2():
#     with open('file2.txt', 'r') as file:
#         result = file.readlines()
#         sleep(2)
#         print(result)
#
# def funcRead3():
#     with open('file3.txt', 'r') as file:
#         result = file.readlines()
#         sleep(3)
#         print(result)
#
# def funcRead4():
#     with open('file4.txt', 'r') as file:
#         result = file.readlines()
#         sleep(4)
#         print(result)
#
# def funcRead5():
#     with open('file5.txt', 'r') as file:
#         result = file.readlines()
#         sleep(5)
#         print(result)
#
# start = time()
# funcRead1()
# funcRead2()
# funcRead3()
# funcRead4()
# funcRead5()
# print(f'Total time: {time()-start}')

# #practice_с
# from random import randint
# from time import time
# import asyncio
#
# for i in range(1,6):
#     with open(f'file{i}.txt', 'w') as file:
#         file.write(str(randint(-10, 10)))
#
# async def funcRead1():
#     with open('file1.txt', 'r') as file:
#         result = file.readlines()
#         await asyncio.sleep(1)
#         print(result)
#
# async def funcRead2():
#     with open('file2.txt', 'r') as file:
#         result = file.readlines()
#         await asyncio.sleep(2)
#         print(result)
#
# async def funcRead3():
#     with open('file3.txt', 'r') as file:
#         result = file.readlines()
#         await asyncio.sleep(3)
#         print(result)
#
# async def funcRead4():
#     with open('file4.txt', 'r') as file:
#         result = file.readlines()
#         await asyncio.sleep(4)
#         print(result)
#
# async def funcRead5():
#     with open('file5.txt', 'r') as file:
#         result = file.readlines()
#         await asyncio.sleep(5)
#         print(result)
#
# async def main():
#     async with asyncio.TaskGroup() as tg:
#         tg.create_task(funcRead1())
#         tg.create_task(funcRead2())
#         tg.create_task(funcRead3())
#         tg.create_task(funcRead4())
#         tg.create_task(funcRead5())
#
# start = time()
# asyncio.run(main())
# print(f'Total time: {time()-start}')