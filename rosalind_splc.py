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

def main():
    fa_list = fa2list('rosalind_splc.txt')
    key = ['UUU', 'UUC', 'UUA', 'UUG', 'UCU', 'UCC', 'UCA', 'UCG', 'UAU', 'UAC', 'UAA', 'UAG', 'UGU', 'UGC', 'UGA', 'UGG', 'CUU', 'CUC', 'CUA', 'CUG', 'CCU', 'CCC', 'CCA', 'CCG', 'CAU', 'CAC', 'CAA', 'CAG', 'CGU', 'CGC', 'CGA', 'CGG', 'AUU', 'AUC', 'AUA', 'AUG', 'ACU', 'ACC', 'ACA', 'ACG', 'AAU', 'AAC', 'AAA', 'AAG', 'AGU', 'AGC', 'AGA', 'AGG', 'GUU', 'GUC', 'GUA', 'GUG', 'GCU', 'GCC', 'GCA', 'GCG', 'GAU', 'GAC', 'GAA', 'GAG', 'GGU', 'GGC', 'GGA', 'GGG']
    pro = ['F', 'F', 'L', 'L', 'S', 'S', 'S', 'S', 'Y', 'Y', 'Stop', 'Stop', 'C', 'C', 'Stop', 'W', 'L', 'L', 'L', 'L', 'P', 'P', 'P', 'P', 'H', 'H', 'Q', 'Q', 'R', 'R', 'R', 'R', 'I', 'I', 'I', 'M', 'T', 'T', 'T', 'T', 'N', 'N', 'K', 'K', 'S', 'S', 'R', 'R', 'V', 'V', 'V', 'V', 'A', 'A', 'A', 'A', 'D', 'D', 'E', 'E', 'G', 'G', 'G', 'G']
    codon_dict = dict(zip(key, pro))
    dna = fa_list[0][1]
    introns = [x[1] for x in fa_list[1:]]
    introns = sorted(introns, key = len, reverse=True)
    for intron in introns:
        dna = dna.replace(intron, '')
    rna = dna.replace('T', 'U')
    codons = []
    for i in range(0,len(rna),3):
        codons.append(rna[i:i+3])
    start = min([i for i,x in enumerate(codons) if x =='AUG'])
    end = min([i for i,x in enumerate(codons) if x in ['UAA', 'UGA', 'UAG']])
    protein = ''.join([codon_dict[x] for x in codons[start:end]])
    return(protein)

if __name__ == '__main__':
    print(main())