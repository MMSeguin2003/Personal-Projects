n = input("Enter a nonnegative integer n to get the first n primes.\n")

class primes:
    def __init__(self):
        self.primes = [2]
    
    def primality(self, n):
        for j in self.primes:
            if n%j == 0:
                return False
            elif j*j > n:
                return True

    def first_n_primes(self, n):
        if n == 0:
            return []
        elif n < 0:
            raise Exception("Enter a nonnegative number.")
        elif n%1 != 0:
            raise Exception("Enter an integer.")
        else:
            j = 3
            k = 2
            print("1: " + str(self.primes[-1]))
            while len(self.primes) < n:
                if self.primality(j):
                    self.primes.append(j)
                    print(str(k) + ": " + str(self.primes[-1]))
                    k += 1
                j += 2
            return self.primes

list = primes()
t = list.first_n_primes(float(n))
if not t:
    print(t)