# print ("Hello World")
# import nympy as np
# print ("Hello, World")
# month = input ("Какой месяц сейчас?")
# print ("December-", month)
# name = input("Anna:")
# print("Anna")
# print("Hello,World!")
# print ("How r u?")
# int_num=int(input('Введите целое число:'))
# print(int_num)
# print(type(int_num))
#
# wow='WOW'
# print(wow*5)
# age=25
# my_age="I'm %d years old" % (age)
# print(my_age)

# pi = 31.4159265
# print("%.4e" % (pi))

# string = input("Введите числа через пробел:")
# list_of_strings = string.split()
# list_of_numbers = list(map(int,list_of_strings))
# print(sum(list_of_numbers[::3]))
# age=19
# if (age>=18):
#     print('u can come in')
# x = int(input ("Vvedite 1 chislo:"))
# y = int(input ("Vvedite 2 chislo:"))
#
# def sum(a,b):
#     return a+b
#
# print(sum(x,y))
# def hello():
#     print("HiHihi")
# hello()
# hello()
# hello()
# name="helloooo hiii hi!"
# for i in name:
#     print(i)
#
#
# L=list(map(float,input().split()))
# L[0], L[-1] = L[-1], L[0]
# L.append(sum(L))
# print(L)

# L=[3.3, 4.4, 5.5, 6.6]
# print(map(round,L))
# print(list(map(round,L)))
# L = ['3.3', '4.4', '5.5', '6.6']
# print(list(map(float, L)))

# person={'name': 'Ivan Petrov'}
# person['age']= 25
# print(person)

# d = {'day' : 22, 'month' : 6, 'year' : 2015}
# print("||".join(d.keys()))

# title = input('Название книги')
# author = input('Фамилия автора')
# year = int(input('Год выпуска'))
#
# book={"title": title, "author": author, "year": year}
# print(book)

# a={'a', 'b', 'c', 'd'}
# print(a)
#
# L = [1,1,2,3,2]
#
# b = set(L)
#
# print(b)


# text = input("Введите текст:")
#
# unique = list(set(text))
#
# print("Количество уникальных символов: ", len(unique))
#

# text = input("Введите текст:")
#
# print(list(set(text)))
#
# print("Количество уникальных символов: ", len(unique))
#
#
# title =input('Алиса в стране чудес')
# author = input('Кэрролл')
# year = int(input('grbrb'))
#
# book={"title": "title", "author": "author", "year": "year"}
# print(book)

# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
#
# a_set, b_set = set(a), set(b)
#
# a_and_b = a_set.union(b_set)
#
# print(a_and_b)
#
#
# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])'/
#
# shopping_center[-1].append("Uniqlo")
# list_id_after = id(shopping_center[-1])
# print(list_id_before is list_id_after )

money = int(input("Ввести суму, которую планируете положить под проценты:"))
per_sent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

ТКБ = int((per_sent['ТКБ'])*(money/100))
СКБ = int((per_sent['СКБ'])*(money/100))
ВТБ = int((per_sent['ВТБ'])*(money/100))
СБЕР = int((per_sent['СБЕР'])*(money/100))

deposit = [ТКБ, СКБ, ВТБ, СБЕР]

print("Накопленные средства за год вклада в каждом из банков=",deposit)

print("Максимальная сумма, которую вы можете заработать:", max(deposit))



# print(int(100000/100))
# print(int(1000*5.6))
# print(int(1000*5.9))
# print(int(1000*4.28))
# print(int(1000*4.0))
#
# deposit = [5600, 5900,4280, 4000]
# print(max(deposit))







