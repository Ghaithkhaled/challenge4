
def fib(n):

        a = 0
        b = 1

        for i in range(1,n):
            c = a + b
            a = b
            b = c
        return b 
for i in range(1,16):
    print("Getal(",i,")=", fib(i))





