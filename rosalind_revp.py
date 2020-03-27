def dna_reverse(dna_str):
    rev = dna_str.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g').upper()[::-1]
    return(rev)

with open('rosalind_revp.txt', 'r') as f:
    dna = ''.join(f.readlines()[1:]).replace('\n', '')

palindromes = []
for i in range(0,len(dna)-3):
    for ii in range(min(i+12, len(dna)), i+3, -1):
        sub_dna = dna[i:ii]
        if(dna_reverse(sub_dna) == sub_dna):
            palindromes.append([i+1,ii-i])

pal_print = [' '.join([str(x) for x in X]) for X in palindromes]
print('\n'.join(pal_print))