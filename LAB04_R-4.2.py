def power(x, n):
    if n==0:
        return 1
    else:
        partial = power(x, n//2)
        result = partial*partial
        if n%2 == 1:
            result *= x
        return result

"""
For this implementation (x =2, n = 18), the trace is:

power(2,18) return 512*512 = 262144
    power (2,9) return 2*16*16 = 512
        power (2,4)  return 4*4 = 16
            power (2,2)  return 2*2 = 4
                power (2,1)   return (1*1)*2 = 2
                    power (2,0)   return 1

"""
print (power(2,18))
