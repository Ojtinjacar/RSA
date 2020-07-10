import random
RangoIni = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
RangoFin = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

def FuncionPhi():
    primoA = numprimo()
    primoB = numprimo()
    z = primoA*primoB
    o = (primoA-1)*(primoB-1)
    return o,z

def numprimo():
    flag = False
    while flag != True:
        sumtres = 0
        a = random.randint(RangoIni, RangoFin)
        b = str(a)
        for d in b:
            sumtres = sumtres + int(d)
        c = b[len(b) - 1]
        if int(c) != 2 and int(c) != 4 and int(c) != 5 and int(c) != 6 and int(c) != 8 and int(c) != 0 and (
                sumtres % 3) > 0:
            y = EsPrimoo(a, 4)
            flag = y
    return a

def hallarclavepublica(i,z):
    flag = False
    while flag != True:
        k = numprimo()
        if k % i != 0:
            flag = True
    return z,k

def hallarclaveprivada(u,e,o):
    a = AlgoritmoEuclides(e, o)
    return u,a

def AlgoritmoEuclides(a, b):
    if b == 0:
        return 0

    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1

    while b != 0:
        q = a // b
        r = a - b * q
        u = u0 - q * u1
        v = v0 - q * v1
        # Update a,b
        a = b
        b = r
        # Update for next iteration
        u0 = u1
        u1 = u
        v0 = v1
        v1 = v

    return v0

def CifrarMensaje(number,ClavePublica1,ClavePublica2):
    Final = pow(number, ClavePublica2, ClavePublica1)
    return Final

def decifrarMensaje(number,ClavePrivada1,ClavePrivada2):
    NumberDes = pow(number, ClavePrivada2, ClavePrivada1)
    return NumberDes

def TestMiller(d, n):
    a = 2 + random.randint(1, n - 4)
    x = pow(a, d, n)

    if (x == 1 or x == n - 1):
        return True
    while (d != n - 1):
        x = (x * x) % n
        d *= 2
        if (x == 1):
            return False
        if (x == n - 1):
            return True
    return False

def EsPrimoo(n, k):
    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True
    d = n - 1
    while (d % 2 == 0):
        d //= 2
    for i in range(k):
        if (TestMiller(d, n) == False):
            return False

    return True

print("Ingresa el numero que quieres codificar:")
a = input()
h = -1
while h < 0:
        p = FuncionPhi()
        ClavePublica = hallarclavepublica(p[0], p[1])
        ClavePrivada = hallarclaveprivada(p[1], p[0], ClavePublica[1])
        h = ClavePrivada[1]
        y = CifrarMensaje(int(a), ClavePublica[0], ClavePublica[1])
print("¡Perfecto! Comparte la siguiente clave privada con tu compañero.")
print(ClavePrivada[0])
print(ClavePrivada[1])
print("Y este es el número codificado:")
print(y)
print("............................................")

print("¡Hola!, Ingresa el número codificado:")
NumCod = input()
print("Ingresa el primer valor de la clave privada")
Val1 = input()
print("Ingresa el segundo valor de la clave privada")
Val2 = input()
print("Si ingresaste los datos correctamente, tu número descodificado es este:")
print(decifrarMensaje(int(NumCod), int(Val1), int(Val2)))
