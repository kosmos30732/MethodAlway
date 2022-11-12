import math
import random
import sympy
import numpy

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

def jacobi(a,n):
    if a==0:
        return 0
    if a==1:
        return 1
    k=0
    while(a%2==0):
        a=a/2
        k+=1
    s=0
    if k%2==0:
        s=1
    else:
        if n%8==1 or n%8==7:
            s=1
        else:
            s=-1

    if n%4==3 and a%4==3:
        s=-s
    if a==1:
        return s
    else:
        return s*jacobi(n%a,a)

def quad_residue(n):
    if sympy.isprime(n):
        return n
    s=[-1,2]
    k=len(str(n))-1
    if k<=4:
        k=3
    a_k=3
    b_k=5
    c_k=7
    i_k=3
    while True:
        k+=1
        while(i_k!=k+1):
            if sympy.isprime(a_k) and jacobi(n,a_k)==1:
                s.append(a_k)
                i_k+=1
            a_k=b_k
            b_k=c_k
            c_k=a_k+6
        m=math.floor(n ** (0.5))
        t=k
        xx=0
        v=[]
        arr_a=[]
        arr_b=[]
        #print("Факторная база создана для k=",k)
        while True:
            t+=1
            while(len(v)!=t):
                e=[]
                a=xx+m
                b=a*a-n
                tmp_b=b
                if b<0:
                    e.append(1)
                    b=-b
                else:
                    e.append(0)
                for i in range(1,len(s)):
                    count=0
                    while (b%s[i]==0):
                        count+=1
                        b=b//s[i]
                    e.append(count)
                if b==1:
                    v.append(e)
                    arr_a.append(a)
                    arr_b.append(tmp_b)
                if xx<=0:
                    xx-=1
                    xx=-xx
                else:
                    xx=-xx
            for i in range(0,t):
                for j in range(0,k):
                    v[i][j]%=2
            #print("Найдено t",t," уравнений")
            vv=numpy.array(v)
            rnd=numpy.zeros((1,t),dtype=int)
            rnd[0][k]+=1
            zero=numpy.zeros((1,k),dtype=int)
            for i in range(0,(2**t)-2):
                tmp=numpy.dot(rnd,vv)
                for j in range(0,k):
                    tmp[0][j]%=2
                if numpy.array_equal(tmp,zero):
                    #print(rnd)
                    x=1
                    b=1
                    for j in range(0,t):
                        if rnd[0][j]==1:
                            x*=arr_a[j]
                            b*=arr_b[j]
                    y=math.floor(b ** (0.5))
                    if x%n!=y%n and x%n!=(-y)%n:
                        res=math.gcd(x+y,n)
                        if res!=1:
                            print("\nФакторная база на k=",k," элементов ", s)
                            print("\nМатрица")
                            for l in v:
                                print(l)
                            print("\nРешение ", rnd)
                            print("\nМассив a ", arr_a)
                            print("\nМассив b ", arr_b)
                            print("\nПроизведение всех a=",x,"\nПроизведение всех b=",b)
                            return res
                rnd[0][k]+=1
                j=k
                while(j!=0):
                    if rnd[0][j]==2:
                        rnd[0][j]=0
                        rnd[0][j-1]+=1
                    j-=1
            #print("Цикл поиска закончен для t=",t)
            if t==k+4:
                break
        
def arr_func(e):
    return e[1]

def get_gen(n):
    phi=n-1
    del_phi=[2]
    a=3
    b=5
    c=7
    while phi%2==0:
        phi=phi//2
    while phi!=1:
        if phi%a==0 and sympy.isprime(a):
            del_phi.append(a)
            while phi%a==0:
                phi=phi//a
        a=b
        b=c
        c=a+6

    g=2
    flag=1
    while(1):
        if pow(g,n-1)%n==1 and pow(g,(n-1)//2)%n!=1:
            for j in del_phi:
                if pow(g,(n-1)//j)%n==1:
                    g=g+1
                    flag=0
                    break
            if flag:
                return g    
        else:
            g=g+1
        flag=1

def gelfond(g,n,a):
    h=math.floor(math.sqrt(n-1))+1
    b=int(pow(g,h))%n
    
    gs=[]
    tmp=1
    for i in range(1,h+1):
        tmp=(tmp*b)%n
        tmp_gs=[i,tmp]
        gs.append(tmp_gs)
    
    gs.sort(key=arr_func)
    
    u=0
    v=0
    tmp=a
    for i in range(1,h+1):
        tmp=(tmp*g)%n
        mid=h//2
        low=0
        high=h-1

        while gs[mid][1]!=tmp and low<=high:
            if tmp>gs[mid][1]:
                low=mid+1
            else:
                high=mid-1
            mid=(low+high)//2
        if low>high:
            continue
        else:
            v=i
            u=gs[mid][0]
            break
    return (h*u-v)%(n-1)


while(1):
    n = int(input("Ввод n="))
    a = int(input("Ввод a="))
    g=get_gen(n)
    x=gelfond(g,n,a)
    print("Образующий =",g,"\nИскомый показатель =",x)
    print("Проверка",g,"^",x,"=",pow(g,x)%n,"(mod",n,")\n")