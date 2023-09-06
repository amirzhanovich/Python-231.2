# #practice_1
# def calc(a, b, operation):
#     if operation == 1:
#         return a+b
#     elif operation == 2:
#         return a-b
#     elif operation == 3:
#         return a*b
#     elif operation == 4:
#         try:
#             return a/b
#         except ZeroDivisionError:
#             return "Число не делится на ноль"
#     else:
#         return "Операция не поддерживается"
#
# x = int(input("Выберите один из операции: 1-Сложить, 2-Вычесть, 3-Умножить, 4-Разделить: "))
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# result = calc(a,b,x)
# print(result)

# #practice_2
# lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 13, 4, 555, 9, 20]
# new_lst = []
# for elem in lst:
#     if elem != 13:
#         if elem % 2 != 0:
#             new_lst.append(elem)
#     else:
#         break
# print(new_lst)

# #practice_3
# new_lst = []
# for i in range(10,0,-1):
#     if i % 2 != 0:
#         if i == 1:
#             new_lst.append(i+1)
#         else:
#             new_lst.append(i*2)
#     else:
#         pass
#
# print(new_lst)

# #practice_4
# lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
# lst1 = []
# lst2 = []
# for elem in lst:
#     if elem<30 and elem%3==0:
#         lst1.append(elem)
#     else:
#         lst2.append(elem)
#
# print(lst1)
# print(sum(lst2))

# #practice_5
# def month_to_season(month):
#     if month == 1 or month == 2 or month == 12:
#         print("Зима")
#     elif month == 3 or month == 4 or month == 5:
#         print("Весна")
#     elif month == 6 or month == 7 or month == 8:
#         print("Лето")
#     elif month == 9 or month == 10 or month == 11:
#         print("Осень")
#
# month_to_season(3)
# month_to_season(7)
# month_to_season(10)
# month_to_season(12)

# #practice_6
# word = "Пришла зима".split()
# word[0], word[1] = word[1], word[0]
# print(word)







