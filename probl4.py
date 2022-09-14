print("N MAI MARE CA M !")

m=int(input("Dati m = "))
n=int(input("Dati n = "))

def factorial(nr):
    p=1
    s=0
    for i in range(1,nr+1):
        p*=i
    return p

#C = n! / (m!(n-m)!)

josc= factorial(m) * (factorial (n-m))

c= factorial(n) / josc

print(c)