def is_perfect_number(n):
    divisors_sum = sum([x for x in range(1, n) if n % x == 0])
    return divisors_sum == n

i=0
while True:
    if is_perfect_number(i):
        print("perfect >>> ",i)
    else:
        pass
        #print("not perfect >>> ",i)
    i= i+1
        