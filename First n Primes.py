class primes:
    def __init__(self, n):
        self.primes = [2]
        self.first_n_primes(n = n)
    
    def primality(self, n):
        for j in self.primes:
            if n%j == 0:
                return False
            elif j**2 > n:
                return True

    def __str__(self):
        k = 1
        for j in self.primes:
            print(f"{k}: " + str(j))
            k += 1
        return(", ".join([str(i) for i in self.primes]))

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
            while len(self.primes) < n:
                if self.primality(j):
                    self.primes.append(j)
                    k += 1
                j += 2
            return(self.primes)