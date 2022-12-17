import math
import random
import sympy
import numpy
from sympy.abc import x
from sympy import degree, GF, rem, gcd
from sympy.ntheory import factorint
#import taichi as ti
#ti.init(arch=ti.cpu)

def alway(n: int) -> int:
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
    x = math.floor(math.sqrt(n))
    if x * x == n:
        return x, x
    while 1:
        x += 1
        if x == (n + 1) / 2:
            print("n - простое")
            return
        else:
            z = x * x - n
            y = math.floor(math.sqrt(z))
            if y * y == z:
                return x + y, x - y
            else:
                continue


def fxc(x, c, n):
    return (x * x + c) % n


def polard(n):
    times = 5
    a = 2
    b = 2
    c = 1
    while 1:
        a = fxc(a, c, n)
        b = fxc(fxc(b, c, n), c, n)

        if a == b:
            if times != 0:
                times -= 1
                c = random.randint(2, 1000)
                continue
            else:
                print("Без результата")
                return
        d = math.gcd(abs(a - b), n)
        if d == 1:
            continue
        else:
            return d


def jacobi(a, n):
    if a == 0:
        return 0
    if a == 1:
        return 1
    k = 0
    while a % 2 == 0:
        a = a / 2
        k += 1
    s = 0
    if k % 2 == 0:
        s = 1
    else:
        if n % 8 == 1 or n % 8 == 7:
            s = 1
        else:
            s = -1

    if n % 4 == 3 and a % 4 == 3:
        s = -s
    if a == 1:
        return s
    else:
        return s * jacobi(n % a, a)


def quad_residue(n):
    if sympy.isprime(n):
        return n
    s = [-1, 2]
    k = len(str(n)) - 1
    if k <= 4:
        k = 3
    a_k = 3
    b_k = 5
    c_k = 7
    i_k = 3
    while True:
        k += 1
        while i_k != k + 1:
            if sympy.isprime(a_k) and jacobi(n, a_k) == 1:
                s.append(a_k)
                i_k += 1
            a_k = b_k
            b_k = c_k
            c_k = a_k + 6
        m = math.floor(n ** (0.5))
        t = k
        xx = 0
        v = []
        arr_a = []
        arr_b = []
        # print("Факторная база создана для k=",k)
        while True:
            t += 1
            while len(v) != t:
                e = []
                a = xx + m
                b = a * a - n
                tmp_b = b
                if b < 0:
                    e.append(1)
                    b = -b
                else:
                    e.append(0)
                for i in range(1, len(s)):
                    count = 0
                    while b % s[i] == 0:
                        count += 1
                        b = b // s[i]
                    e.append(count)
                if b == 1:
                    v.append(e)
                    arr_a.append(a)
                    arr_b.append(tmp_b)
                if xx <= 0:
                    xx -= 1
                    xx = -xx
                else:
                    xx = -xx
            for i in range(0, t):
                for j in range(0, k):
                    v[i][j] %= 2
            # print("Найдено t",t," уравнений")
            vv = numpy.array(v)
            rnd = numpy.zeros((1, t), dtype=int)
            rnd[0][k] += 1
            zero = numpy.zeros((1, k), dtype=int)
            for i in range(0, (2**t) - 2):
                tmp = numpy.dot(rnd, vv)
                for j in range(0, k):
                    tmp[0][j] %= 2
                if numpy.array_equal(tmp, zero):
                    # print(rnd)
                    x = 1
                    b = 1
                    for j in range(0, t):
                        if rnd[0][j] == 1:
                            x *= arr_a[j]
                            b *= arr_b[j]
                    y = math.floor(b ** (0.5))
                    if x % n != y % n and x % n != (-y) % n:
                        res = math.gcd(x + y, n)
                        if res != 1:
                            print("\nФакторная база на k=", k, " элементов ", s)
                            print("\nМатрица")
                            for l in v:
                                print(l)
                            print("\nРешение ", rnd)
                            print("\nМассив a ", arr_a)
                            print("\nМассив b ", arr_b)
                            print(
                                "\nПроизведение всех a=", x, "\nПроизведение всех b=", b
                            )
                            return res
                rnd[0][k] += 1
                j = k
                while j != 0:
                    if rnd[0][j] == 2:
                        rnd[0][j] = 0
                        rnd[0][j - 1] += 1
                    j -= 1
            # print("Цикл поиска закончен для t=",t)
            if t == k + 4:
                break


def arr_func(e):
    return e[1]


def get_gen(n):
    phi = n - 1
    del_phi = [2]
    a = 3
    b = 5
    c = 7
    while phi % 2 == 0:
        phi = phi // 2
    while phi != 1:
        if phi % a == 0 and sympy.isprime(a):
            del_phi.append(a)
            while phi % a == 0:
                phi = phi // a
        a = b
        b = c
        c = a + 6
    g = 2
    flag = 1
    while 1:
        if pow(g, n - 1) % n == 1 and pow(g, (n - 1) // 2) % n != 1:
            for j in del_phi:
                if pow(g, (n - 1) // j) % n == 1:
                    g = g + 1
                    flag = 0
                    break
            if flag:
                return g
        else:
            g = g + 1
        flag = 1


def gelfond(g, n, a):
    h = math.floor(math.sqrt(n - 1)) + 1
    b = int(pow(g, h)) % n
    gs = []
    tmp = 1
    for i in range(1, h + 1):
        tmp = (tmp * b) % n
        tmp_gs = [i, tmp]
        gs.append(tmp_gs)
    gs.sort(key=arr_func)
    tmp = a
    for i in range(1, h + 1):
        tmp = (tmp * g) % n
        mid = h // 2
        low = 0
        high = h - 1
        while gs[mid][1] != tmp and low <= high:
            if tmp > gs[mid][1]:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2
        if low > high:
            continue
        else:
            v = i
            u = gs[mid][0]
            break
    return (h * u - v) % (n - 1)


def func_f(x, y, b, g, n, a):
    if x % 3 == 1:
        x1 = (a * x) % n
        y1 = y
        b1 = (b + 1) % (n - 1)
    elif x % 3 == 2:
        x1 = (x * x) % n
        y1 = (2 * y) % (n - 1)
        b1 = (2 * b) % (n - 1)
    else:
        x1 = (g * x) % n
        y1 = (y + 1) % (n - 1)
        b1 = b
    return x1, y1, b1


def p_Pollard(g, n, a):
    x2 = x1 = 1
    b1 = b2 = y1 = y2 = 0
    while 1:
        x1, y1, b1 = func_f(x1, y1, b1, g, n, a)
        x2, y2, b2 = func_f(x2, y2, b2, g, n, a)
        x2, y2, b2 = func_f(x2, y2, b2, g, n, a)
        if x1 == x2:
            break
    r = (b1 - b2) % (n - 1)
    if r == 0:
        return
    d = math.gcd(r, (n - 1))
    x = (pow(r // d, -1, (n - 1) // d) * (y2 - y1) // d) % ((n - 1) // d)
    if pow(g, x) % n == a:
        return x
    x_0=x
    for k in range(1, d):
        x = x_0 + (n - 1) // d * k
        if pow(g, x) % n == a:
            return x


def gcd_polinom(f,g,mod):
    if len(g)>len(f):
        g,f=f,g
    while(1):
        f=f%mod
        g=g%mod
        g_tmp=g
        while(1):
            
            g=g*f[0]
            for i in range(len(f)-len(g)):
                g=numpy.append(g,0)
            r=f-g
            r=r%mod
            count=0
            for i in r:
                if i==0:
                    count+=1
                else:
                    break
            r=r[count:]
            g=g_tmp
            if len(r)<len(g):
                break
            else:
                f=r
        f=g
        g=r
        if len(g)==0:
            return f
        if len(g)==1 and g[0]==1:
            return numpy.array([1])
   
#print(sympy.polys.galoistools.gf_gcdex(ZZ.map([1,0,-4,0,0,-1,0,4]),ZZ.map([1,-4,-1,0,4]),13,ZZ))

def privodim(f, p):
    u=x
    count=degree(f)//2
    while(count):
        u=rem(pow(u,p),f,domain=GF(p))
        d=gcd(f,u-x,domain=GF(p))
        if d!=1:
            return "приводим"
        count-=1
    return "неприводим"

def primitiv(g,p):
    p_n=pow(p,degree(g))
    p_all=factorint(p_n-1)
    for p_i in p_all:
        r=rem(pow(x,(p_n-1)/p_i),g,domain=GF(p))
        if r==1:
            return "непримитивный"
    return "примитивный"

while(1):
    f=sympy.Poly(input("Введите полином= "))
    p=int(input("Введите p (Z_p)= "))
    print(privodim(f,p))
    print(primitiv(f,p))
