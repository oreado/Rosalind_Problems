def dna2rna(dna,rf):
    rna = []
    for i in range(rf, len(dna), 3):
        rna.append(dna[i:i+3].replace('T', 'U'))
    return(rna)

def find_orf(rna):
    orf = []
    if('AUG' in rna and ('UAA' in rna or 'UAG' in rna or 'UGA' in rna)):
        start_site = [i for i,x in enumerate(rna) if x == 'AUG']
        end_site = [j for j,y in enumerate(rna) if y in ['UAA', 'UAG', 'UGA']]
        for a in start_site:
            if(a < max(end_site)):
                start = a
                end = min([b for b in end_site if b > a])
                orf.append(rna[start:end]) 
    return(orf)

def orf2protein(orf):
    protein = ''.join([codon_table[x] for x in orf])
    return(protein)

with open('rosalind_orf.txt', 'r') as f:
    dna = f.readlines()

dna = ''.join(dna[1:]).replace('\n', '')
dna_rev = dna.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()[::-1]

key = ['UUU', 'UUC', 'UUA', 'UUG', 'UCU', 'UCC', 'UCA', 'UCG', 'UAU', 'UAC', 'UAA', 'UAG', 'UGU', 'UGC', 'UGA', 'UGG', 'CUU', 'CUC', 'CUA', 'CUG', 'CCU', 'CCC', 'CCA', 'CCG', 'CAU', 'CAC', 'CAA', 'CAG', 'CGU', 'CGC', 'CGA', 'CGG', 'AUU', 'AUC', 'AUA', 'AUG', 'ACU', 'ACC', 'ACA', 'ACG', 'AAU', 'AAC', 'AAA', 'AAG', 'AGU', 'AGC', 'AGA', 'AGG', 'GUU', 'GUC', 'GUA', 'GUG', 'GCU', 'GCC', 'GCA', 'GCG', 'GAU', 'GAC', 'GAA', 'GAG', 'GGU', 'GGC', 'GGA', 'GGG']
pro = ['F', 'F', 'L', 'L', 'S', 'S', 'S', 'S', 'Y', 'Y', 'Stop', 'Stop', 'C', 'C', 'Stop', 'W', 'L', 'L', 'L', 'L', 'P', 'P', 'P', 'P', 'H', 'H', 'Q', 'Q', 'R', 'R', 'R', 'R', 'I', 'I', 'I', 'M', 'T', 'T', 'T', 'T', 'N', 'N', 'K', 'K', 'S', 'S', 'R', 'R', 'V', 'V', 'V', 'V', 'A', 'A', 'A', 'A', 'D', 'D', 'E', 'E', 'G', 'G', 'G', 'G']
codon_dict = dict(zip(key, pro))

rnas = list(map(lambda x: dna2rna(dna, x), [0,1,2]))
rnas_rev = list(map(lambda x: dna2rna(dna_rev, x), [0,1,2]))
rnas_all = rnas + rnas_rev

orfs = []
for r in rnas_all:
    orf = find_orf(r)
    orfs += orf

proteins = list(set(map(orf2protein, orfs)))
with open('rosalind_orf_result.txt', 'w') as f:
    f.write('\n'.join(proteins))
print('\n'.join(proteins))