import math
import random

def alway(n : int) -> int:
    d = math.floor(2 * (n ** (1.0 / 3.0)) + 1)
    if d % 2 == 0:
        d += 1
    q = 4 * (math.ceil((n / (d - 2))) - math.ceil((n / d)))
    r1 = n % d
    r2 = n % (d - 2)
    s = math.ceil(n ** (0.5))
    
    while r1 != 0:
        d += 2
        if d > s:
            print("Делителя нет")
            return -1
        r = 2 * r1 - r2 + q
        r2 = r1
        r1 = r
        if r1 < 0:
            r1 += d
            q += 4
        while r1 >= d:
            r1 -= d
            q -= 4
    return d

def ferma(n):
    x=math.floor(math.sqrt(n))
    if x*x==n:
        return x,x
    while(1):
        x+=1
        if x==(n+1)/2:
            print("n - простое")
            return
        else:
            z=x*x-n
            y=math.floor(math.sqrt(z))
            if y*y==z:
                return x+y,x-y
            else:
                continue

def fxc(x,c,n):
    return ((x*x+c)%n)

def polard(n):
    times=5
    a=2
    b=2
    c=1

    while(1):
        a=fxc(a,c,n)
        b=fxc(fxc(b,c,n),c,n)

        if a==b:
            if times!=0:
                times-=1
                c=random.randint(2,1000)
                continue
            else:
                print("Без результата")
                return
        
        d=math.gcd(abs(a-b),n)
        if d==1:
            continue
        else:
            return d


while(1):
    num = int(input())
    print(polard(num))