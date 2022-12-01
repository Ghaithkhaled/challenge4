num1 = float(input("nummer kiezen: "))
while True:
  opr = input("kies hier je operator (+, -, , /,*): ")

  if "+" in opr:
    num2 = float(input("Kies je nieuwe getal: "))
    num1 = float(num1) + float(num2)
    print("tussenuitkomst is", num1)
  elif "-" in opr:
    num2 = float(input("Kies je nieuwe getal: "))
    num1 = float(num1) - float(num2)
    print("tussenuitkomst is", num1)

  elif "*" in opr:
    num2 = float(input("Kies je nieuwe getal: "))
    num1 = float(num1) * float(num2)
    print("tussenuitkomst is", num1)

  elif "/" in opr:
    num2 = float(input("Kies je nieuwe getal: "))
    num1 = float(num1) / float(num2)
    print("tussenuitkomst is", num1)

    print(num1)
    break