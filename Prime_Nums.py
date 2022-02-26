def find_primes (self):
    max_num = self
    prime_nums = []
    # This creates a list of integers from 2 to the number called.
    for i in range(2,max_num):
        prime_nums.append(i)
   # This iterates through the list, removing every number divisible by it. The only numbers remaining will be primes.   
    for num in prime_nums:
        for x in range(num+1,max_num):
            if x % num == 0:
                if x in prime_nums:
                    prime_nums.remove(x)
    return prime_nums

print(find_primes(2000))
