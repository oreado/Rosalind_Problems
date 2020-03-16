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

def seq_overlap(seq1, seq2, name1, name2):
    if(seq1[-3:]==seq2[:3]):
        return(name1 + ' ' + name2)

fa_list = fa2list('rosalind_grph.txt')

result = []
for i in range(len(fa_list)):
    name1 = fa_list[i][0]
    seq1 = fa_list[i][1]
    other = fa_list[:]
    other.pop(i)
    for ii in range(len(other)):
        name2 = other[ii][0]
        seq2 = other[ii][1]
        overlap = seq_overlap(seq1,seq2,name1,name2)
        if(overlap):
            result.append(overlap)

with open('rosalind_grph_result.txt', 'r') as f1:
    f1.write('\n'.join(result))