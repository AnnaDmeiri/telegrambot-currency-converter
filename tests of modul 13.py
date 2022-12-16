# print('3' in str (1234567))
# print('7' in str (1234567))
# print('9' in str (1234567))

# a= [1,2,3]
# print(id(a))
#
# b = a
# print(id(b))
#
# print(a is b)

# a= [1,2,3]
# b= [1,2,3]
# print(a==b)
# print(a is b)

# is_rainy = True
# if is_rainy:
#     print('take umbrella')
# else:
#     print('dont take umbrella')


# a= 11
# if a<6:
#     a=a+13
# else:
#     a= a-8
#     print(a)

# s =5
# a = 10
# if a > 0:
#     s = s + a
# else:
#     s = s - a
#     print(s)


# a=-3
# if a<5:
#     a=5
#     print(a)

# a=16
# b=14+a
# print("b=",b)

# a=7
# b=9+a
# print("a=F(",b,")")

# is_rainy = True
# heavy_rain=False
#
# if is_rainy:
#     if heavy_rain:
#         print("take umbrella")
#     else:
#         print("wear dojdevik")
# else:
#     print("dont take umbrella")

# if zero:
#     print(10/ zero)
# else:
#     print(" delit na nol nelzia")
#
# try:
#     print('befor iskluchenie')
#     a= int(input("a:"))
#     b= int(input("b:"))
#     c=a/b
#     print(c)
# except ZeroDivisionError as e:
#     print(e)
#     print("after iskluchenia")
# print("after after iskluchenia")

# age=int(input("How old r u?"))
# if age>100 or age <=0:
#     raise ValueError("u cannot be like this age")
# print(f"тебе {age}лет!")

# num = int(input("inter chislo"))
# if A % 2 == 0:
#     print("Число А кратно 2 ")




#
# if 6<= hour <12:
# print("Утро!")

# if x > 0 and y >0:
#      print("Первая четверть")
# if x > 0 and y < 0:
#      print("Четвертая четверть")
# if x < 0 and y > 0:
#      print("Вторая четверть")
# if x < 0 and y < 0:
#      print("Третья четверть")
#

# name = "hello, world!"
# for i in range(1,11):
#      print(name)

list_= [-5, 2, 4, 8, 12, -7, 5]
print(len(list_) == len(set(list_)))

a = ""
b = "bar"

print(1 and a or b)
