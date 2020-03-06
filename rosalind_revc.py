with open('rosalind_revc.txt', 'r') as f:
    dna = f.readline()
dna1 = dna.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g')
dna2 = dna1.upper()[::-1]
with open('rosalind_revc_result.txt', 'w') as f1:
    f1.write(dna2)