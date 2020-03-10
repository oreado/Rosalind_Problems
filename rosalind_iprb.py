with open('rosalind_iprb.txt', 'r') as f:
    data = f.read()
k,m,n = [int(x) for x in data.split(' ')]

recessive_rate = ((n/(k+m+n)) * ((n-1)/(k+m+n-1)) * 1 + 
                  (n/(k+m+n)) * (m/(k+m+n-1)) * 0.5 + 
                  (m/(k+m+n)) * (n/(k+m+n-1)) *0.5 + 
                  (m/(k+m+n)) * ((m-1)/(k+m+n-1)) * 0.25 
                  )

dominant_rate = 1 - recessive_rate
print(format(dominant_rate, '.5f'))