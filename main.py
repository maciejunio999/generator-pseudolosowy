#   https://pl.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators

def funk1(x):
    if x >= 100:
        a = x ** 2
        b = str(a)
        return (b)
    elif x < 100:
        print("Podana liczba nie pasuje do algorytmu")


def funk2(x):
    l = len(x)
    y = x[1:l - 1]
    return y


def funk3(x, c):
    c = c + x
    return c


def funk4(x):
    y = int(x)
    return y


def funk(x, d, k=""):
    x1 = funk1(x)  # kwadrat x
    x2 = funk2(x1)  # srodek kwadratu x
    funk.x3 = funk3(x2, k)  # dodajemy do ciągu (tu pustego) środek kwadratu x
    x4 = funk4(funk.x3)  # zamieniamy ciąg na liczbę
    if len(funk.x3) < d:
        funk(x4, k, d)
