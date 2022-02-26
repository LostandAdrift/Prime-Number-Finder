

def find_primes (self):
    max_num = self
    prime_nums = []
    for i in range(2,max_num):
        prime_nums.append(i)
    for num in prime_nums:
        for x in range(num+1,max_num):
            if x % num == 0:
                if x in prime_nums:
                    prime_nums.remove(x)
    return prime_nums

print(find_primes(2000))
