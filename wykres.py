import matplotlib.pylab as plt
import numpy as np
from main import funk

funk(122, 100)
a = funk.x3
l = len(funk.x3)
x = []
for i in a:
    x.append(i)
t = np.linspace(0., l, num=l)
# print(x)

wykres = plt.figure(figsize=(12, 9))
plt.scatter(t, x)
plt.grid()
plt.xlabel("t")
plt.ylabel('x')
plt.title("Kolejne liczby pseudolosowe dla 122")
plt.show()
#plt.savefig('122.png')