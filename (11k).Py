def vermenigvuldigen(n1, n2):
    g = n1 * n2
    return g

number1 = (input('enter first number : '))
number2 = (input('enter second number : '))
if number1.isnumeric() == True and number2.isnumeric() == True:
    print (vermenigvuldigen(int(number1), int(number2)))
else: 
    print ('voer een nummer in')