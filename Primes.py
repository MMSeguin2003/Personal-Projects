class primes:
    def __init__(self, find = None):
        self.primes = []
        if isinstance(find, int):
            self.generate_primes(find)
    
    def __is_prime__(self, k):
        for j in self.primes:
            if k % j == 0:
                return(False)
            elif j**2 > k:
                return(True)

    def __str__(self):
        return(", ".join([str(j) for j in self.primes]) + ", ...")

    def generate_primes(self, n):
        if n < 0:
            raise Exception("Enter a non-negative number.")
        if not isinstance(n, int):
            raise Exception("Enter an integer.")
        if n == 0:
            return(self.primes)
        else:
            start_len = len(self.primes)
            if start_len <= 1:
                self.primes = list(range(2, 3 + start_len))
                j = 3 + 2*start_len
            else:
                j = self.primes[start_len-1] + 2
            while len(self.primes) - start_len < n:
                if self.__is_prime__(j):
                    self.primes.append(j)
                j += 2
        return(self.primes)

known_primes = primes(find=1)

def is_prime(n, known = known_primes):
    if n < 0:
        raise Exception("Enter a non-negative number.")
    if not isinstance(n, int):
        raise Exception("Enter an integer.")
    if n <= 1:
        return(False)
    if str(n)[-1] in [str(2*j) for j in range(5)] and n != 2:
        return(False)
    if str(n)[-1] == "5" and n != 5:
        return(False)
    else:
        while known.primes[-1] < int(n**0.5):
            known.generate_primes(1)
        for j in known.primes:
            if n % j == 0:
                return(False)
            elif j**2 > n:
                return(True)

import time
import pandas as pd
from matplotlib import pyplot as plt

x = {"n": [], "Prime Time": []}
for j in range(1,100000):
    x["n"].append(j)
    t0 = time.time()
    is_prime(j)
    t1 = time.time()
    x["Prime Time"].append(t1-t0)
x = pd.DataFrame(x)

plt.figure(figsize=(12, 6))
plt.plot(x["n"], x["Prime Time"], marker = "o")
plt.title("Time to Determine if n is Prime")
plt.xlabel("n")
plt.ylabel("Time")
plt.ticklabel_format(style = "plain", axis = "y")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()