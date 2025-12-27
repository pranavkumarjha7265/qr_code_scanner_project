# n=int(input("n: "))
# for i in range(n):
#     for j in range(n+1):
#         if(i==j or i+j==n):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()





# walrus operator:




# foods=list()
# while(food := input("Enter the food:") != "quit"):
#     foods.append(food)
# print(foods)







# x=input("X:")
# month = {"1":"jan","2":"fab","3":"march","4":"april","5":"may","6":"june","7":"july","8":"august","9":"september","10":"october","11":"november","12":"december"}
# print(month[x])





# n=int(input("N: "))
# for i in range(n):
#     for j in range(n+1):
#         if(i==j):
#             print("\\" , end=" ")
#         elif(i+j==n):
#             print("/",end=" ")
#         else:
#             print(" ",end=" ")
#     print()






# n=int(input("N: "))
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i-1):
#         print("*",end=" ")
#     print()






# x=input("X: ")
# print(eval(x))










# x=input("X:")
# print(f"{x} is very motki,bhaish,lol,pagal.")






import os
choice = input("c: ")
if choice == "y":
    print(os.system("shutdown /s /t 1"))





# import os
# choice = input("c: ")
# if choice == "y":
#     print(os.system("shutdown /r /t 1"))






# import os
# choice = input("c: ")
# if choice == "y":
#     print(os.system("shutdown /l /t 1"))






#swapping of number :

# num1=int(input("num1: "))
# num2=int(input("num2: "))
# print("before swapping num1 and num2 is {},{} respectively".format(num1,num2))
# num3 = num1
# num1 = num2
# num2 = num3
# print("after swapping num1 and num2 is {},{} respectively".format(num1,num2))







# s = input("enter the value:")
# if(s == s[::-1]):
#     print("number is palindrome")
# else:
#     print("not a palindrome")








# CALENDAR OF ANY MONTH OF A SPECIFIC YEAR:

# import calendar
# year = int(input("year: "))
# month = int(input("month: "))
# print(calendar.month(year,month))








# import calendar
# year = int(input("year: "))
# month = int(input("month: "))
# calendar.setfirstweekday(calendar.SUNDAY) #this is use to set the first day of week of the desire calendar.
# print(calendar.month(year,month))







#calandar of whole year:

# import calendar
# year = int(input("year: "))
# print(calendar.calendar(year))







#check for leap year by using calandar module:

# import calendar
# year = int(input("year: "))
# print(calendar.isleap(year))








# display day name as string value:


# import datetime
# current_date = datetime.datetime.now()
# day_name = current_date.strftime("%A")
# print(current_date,day_name)








# a=int(input("a: "))
# b=int(input("b: "))
# option = input("option: ")
# match option:
#     case 'a':
#         print(a+b)
        
#     case 'b':
#         print(a-b)
        
#     case 'c':
#         print(a*b)
#     case 'd':
#         print(a/b)
    








# option=input("option: ")
# a=int(input("a: "))
# b=int(input("b: "))
# def sum(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)
# def div(a,b):
#     print(a/b)
# if option == 'a':
#     sum(a,b)
# elif option == 'b':
#     sub(a,b)
# elif option == 'c':
#     mul(a,b)
# elif option == 'd':
#     div(a,b)
# else:
#     print("operator is not define")










# option=input("option: ")
# a=int(input("a: "))
# b=int(input("b: "))
# def sum():
#     print(a+b)
# def sub():
#     print(a-b)
# def mul():
#     print(a*b)
# def div():
#     print(a/b)
# funct={'a':sum,'b':sub,'c':mul,'d':div}
# f = funct.get(option)
# print(f())








# import calendar
# year=int(input("year: "))
# month=int(input("month: "))
# calendar.setfirstweekday(calendar.SUNDAY)
# print(calendar.month(year,month))





# import datetime
# cur_date = datetime.datetime.now()
# cur_day = cur_date.strftime("%A")
# print(cur_date,cur_day)






# import math
# n=int(input("N: "))
# print(math.factorial(n))





# import random
# print(random.randint(1000,9999))







# import calendar
# month = int(input("month: "))
# year = int(input("year: "))
# calendar.setfirstweekday(calendar.SUNDAY)
# print(calendar.month(year,month))





# data=[]
# while True:
#     name = input("Enter the name: ")
#     data.append(name)

#     choice = input("Enter another name?? (y/n): ")
#     if choice.casefold() == 'n': 
#         break 
# for element in data:
#     print(element)                  
                









# n=int(input("N: "))
# for i in range(1,n+1):
#     if n % i == 0:
#         print("Factors of the number is: ",i)







# year=int(input("YEAR: "))
# if year % 4 == 0:
#     if year % 100 ==0:
#         if year % 400 == 0:
#             print("leap year")
#         else:
#             print("not leap year")
#     else:
#         print("leap year")
# else:
#     print("not a leap year")





# import os
# print(os.system("shutdown /r /t 1"))






# import calendar
# year=int(input("year: "))
# print(calendar.calendar(year))







a=eval(input(""))
print(a)