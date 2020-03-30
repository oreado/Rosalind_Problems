def factorial(n):
    result = 1
    for i in range(1,n+1):
        if(i==1):
            result = 1
        else:
            result = i*result
    return(result)

def combin(n, N):
    return(factorial(N)/(factorial(n)*factorial(N-n)))

k = int(input('k = :'))
n = int(input('n = :'))

p = 0
for i in range(n, 2**k+1):
    p_i = combin(i, 2**k)*(0.25 ** i) * (0.75 ** (2**k - i))
    p += p_i

print('%.3f'%p)