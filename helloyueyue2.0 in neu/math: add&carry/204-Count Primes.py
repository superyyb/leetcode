#Best solution: time: O(n*loglog n)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
        return sum(is_prime)
    '''
    n = 28
    2->is_prime: 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26 -> not is_prime
    3->is_prime: 9, 12, 15, 18, 21, 24, 27 -> not is_prime
    '''


#Got TLE time: O(n^1.5)
class Solution:
    def countPrimes(self, n: int) -> int:
        '''
        Rule: A × B = num then whether A or B is smaller than num**0.5

        Check whether a number is prime number and count the amount
        1.Define a function to check prime numbers
        2.Traverse from 2 to n, count the amount of prime numbers

        Case: n = 10  prime number: 2,3,5,7
        '''

        def isPrime(num: int) -> bool:
            if num <= 1:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        count = 0
        for i in range(2, n):
            if isPrime(i):
                count += 1
        return count

