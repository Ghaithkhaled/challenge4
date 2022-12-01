# import datetime

# n = int(input("wat is je geboortedatum?"))
# print(n)
# if n > 20050101:

#  print("je mag motorrijden")

# elif n < 20050101:
#   print("je mag niet motorrijden")




# # import datetime 
# # now = datetime.datetime.now()
# now.strftime("%y-%m-%d")

# n = int(input("wat is je geboortedatum?"))
# print(n)
# if  now < 20040101:
#     print("je mag niet motorrijden")
# elif  > 20040101:
#   print("je mag niet motorrijden")

# from datetime import date
# age = int(input("wat is je geboortedatum?")) 
# def age(birthdate):
#     today = date.today()
#     age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
#     return age 
# print(date(age)) 


# while True:
#     try:
#         checker = int(age)
#         if checker >= 21 :
#             print("you can ride big")
#             break
#         elif checker >= 19 :
#                 print("you can ride mid")
#         elif checker >= 17 :
#                 print("you can ride small")
#         break 
#     except:
#         print("An exception occurred")
# print(checker)



# def myAge(year):
#      return 2022-year

# year= int(input("enter ff"))
# print(myAge(year))


import datetime

def geboortedatum():

    datum = input('wat is uw geboortedatum? (YYYY-MM-DD): ')

    try:

        Juiste_datum = datetime.datetime.strptime(datum, "%Y-%m-%d")

        if datum < ("2005-01-01"):

            print("volges de wet mag jij voor een moter rijbewijs gaan!")

        elif datum > ("2005-01-01"):

            print("volges de wet mag jij niet voor een moter rijbewijs gaan!")        

    except ValueError:

        print("Sorry, dat is niet juist. Probeer het opnieuw!")

        return geboortedatum()



print(geboortedatum())