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

seq_list = fa2list('rosalind_sseq.txt')
seq1 = seq_list[0][1]
seq2 = seq_list[1][1]

indices = []
pos = 0
for i in range(len(seq2)):
    find = seq1.find(seq2[i])
    seq1 = seq1[(find + 1):]
    pos = pos + find + 1
    indices.append(pos)

with open('rosalind_sseq_result.txt', 'w') as f1:
    f1.write(' '.join([str(x) for x in indices]))