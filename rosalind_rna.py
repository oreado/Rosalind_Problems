with open('rosalind_rna.txt', 'r') as f:
    dna = f.read()
rna = dna.replace('T', 'U')
with open('rosalind_rna_result.txt', 'w') as f1:
    f1.write(rna)