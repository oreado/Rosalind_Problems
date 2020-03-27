mass_table =(
'''A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333'''
)
mass_table = mass_table.split('\n')
mass_table = [x.split('   ') for x in mass_table]
aas = [x[0] for x in mass_table]
weight = [float(x[1]) for x in mass_table]
mass_dict = dict(zip(aas, weight))
with open('rosalind_prtm.txt', 'r') as f:
    aa_str = f.read().replace('\n','')
aa_weight = [mass_dict[x] for x in aa_str]
aa_weight_sum = sum(aa_weight)
print('%.3f' % aa_weight_sum)