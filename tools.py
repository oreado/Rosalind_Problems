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

key = ['UUU', 'UUC', 'UUA', 'UUG', 'UCU', 'UCC', 'UCA', 'UCG', 'UAU', 'UAC', 'UAA', 'UAG', 'UGU', 'UGC', 'UGA', 'UGG', 'CUU', 'CUC', 'CUA', 'CUG', 'CCU', 'CCC', 'CCA', 'CCG', 'CAU', 'CAC', 'CAA', 'CAG', 'CGU', 'CGC', 'CGA', 'CGG', 'AUU', 'AUC', 'AUA', 'AUG', 'ACU', 'ACC', 'ACA', 'ACG', 'AAU', 'AAC', 'AAA', 'AAG', 'AGU', 'AGC', 'AGA', 'AGG', 'GUU', 'GUC', 'GUA', 'GUG', 'GCU', 'GCC', 'GCA', 'GCG', 'GAU', 'GAC', 'GAA', 'GAG', 'GGU', 'GGC', 'GGA', 'GGG']
pro = ['F', 'F', 'L', 'L', 'S', 'S', 'S', 'S', 'Y', 'Y', 'Stop', 'Stop', 'C', 'C', 'Stop', 'W', 'L', 'L', 'L', 'L', 'P', 'P', 'P', 'P', 'H', 'H', 'Q', 'Q', 'R', 'R', 'R', 'R', 'I', 'I', 'I', 'M', 'T', 'T', 'T', 'T', 'N', 'N', 'K', 'K', 'S', 'S', 'R', 'R', 'V', 'V', 'V', 'V', 'A', 'A', 'A', 'A', 'D', 'D', 'E', 'E', 'G', 'G', 'G', 'G']
codon_dict = dict(zip(key, pro))


def fa2list(fasta_file):
    with open(fasta_file, 'r') as f:
        fa = f.read().split('>')
    del(fa[0])
    fa = [x.rstrip() for x in fa]
    fa_list = [x.split('\n') for x in fa]
    for i in range(len(fa_list)):
        fa_list[i][1] = ''.join(fa_list[i][1:])
        del(fa_list[i][2:])
    return(fa_list)



