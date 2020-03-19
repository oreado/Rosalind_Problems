data = input('The number of couples: ')
a1,a2,a3,a4,a5,a6 = [int(x) for x in data.split(' ')]
E = (a1+a2+a3+0.75*a4+0.5*a5)*2
print(E)