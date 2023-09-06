from time import time, sleep
from threading import Thread

# #practice_1
# a1 = time()
# sleep(1)
# with open('1.txt', 'w') as file1:
#     a2 = time()
#     print(a2-a1)
#     file1.write("file1")

# #practice_2
# a1 = time()
# for i in range(1,101):
#     sleep(1)
#     with open('file.txt', 'w') as file:
#         file.write("file")
# a2 = time()
# print(a2-a1)

# #practice_3
# def file():
#     sleep(1)
#     with open('file.txt', 'w') as file:
#         file.write("file")
#
# a1 = time()
# for i in range(100):
#     th = Thread(target=file, args=())
#     th.start()
# a2 = time()
# print(a2-a1)