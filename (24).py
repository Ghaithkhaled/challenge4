


# from datetime import date 

# # day2= date(1999, 5,22)

# num1 = date(input("nummer kiezen: "))
# day1= date.today()

# diff= (day1 , num1)
# print(diff.days, "dats so far")




# n1 = input("In welke jaar ben je geboren ?")
# days = int(n1) *365

# n2 = input("In welke maand ben je geboren ?")
# month = int(n2) *30

# n3 = input("In welke dag ben je geboren ?")
# day = int(n3) *1

# print("uw leeftijd in dagen is", n1 + n2 + n3 )


# from datetime import date


# num1 = input("")
# dt_today = date.today()
# n= dt_today- num1


# print(n.days)

# print('Enter your birth date in the following format: \nDD/MM/YYYY')
# birth_date = input()

# birth_day = int(birth_date.split('/')[0])
# birth_month = int(birth_date.split('/')[1])
# birth_year = int(birth_date.split('/')[2])

# current_year = 2022
# current_month = 11
# current_day = 28

# extra_days = ((current_year - birth_year) // 4) + ((current_year - birth_year) // 400) + 1

# this_year_days = 67 #Jan=31, Feb=28, Mar=8th

# birth_year_days = birth_day + ((birth_month - 1)*30)

# total_days = ((current_year - birth_year)*365) + (this_year_days + birth_year_days) + extra_days

# print(total_days)


print("now enter your age")
age = int(input("age: "))
days = age * 365

print(days,"days")