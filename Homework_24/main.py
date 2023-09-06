# #practice_1
# from random import randint
# from time import time, sleep
#
# def function():
#     with open('file1.txt', 'w') as file1:
#         sleep(1)
#         file1.write(str(randint(-10, 10)))
#
# a1 = time()
# f = function()
# a2 = time()
# print(a2 - a1)

# #practice_2
# from random import randint
# from time import time, sleep
#
# def function():
#     with open('file2.txt', 'w') as file2:
#         sleep(1)
#         file2.write(str(randint(-10, 10)))
#
# a1 = time()
# for i in range(1000):
#     f = function()
# a2 = time()
# print(a2-a1)

# #practice_3
# from random import randint
# from time import time, sleep
# from multiprocessing import Process
#
# def function():
#     with open('file3.txt', 'a') as file3:
#         sleep(1)
#         file3.write(str(randint(-10, 10))+"\n")
#
# if __name__ == "__main__":
#     number_task = 1000
#     procs = []
#     proc = Process(target=function)
#     procs.append(proc)
#     proc.start()
#
#     a1 = time()
#
#     for name in range(number_task):
#         proc = Process(target=function, args=())
#         procs.append(proc)
#         proc.start()
#
#     for proc in procs:
#         proc.join()
#
#     a2 = time()
#     print(a2-a1)
