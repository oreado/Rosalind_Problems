import numpy as np
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

fa_list = fa2list('rosalind_pdst.txt')

matrix = np.zeros((len(fa_list),len(fa_list)))

seq_list = [x[1] for x in fa_list]
seq_len = len(seq_list[0])

for i in range(len(seq_list)):
    seq1 = seq_list[i]
    for ii in range(i+1, len(seq_list)):
        seq2 = seq_list[ii]
        diff = sum([a != b for a, b in zip(seq1, seq2)])
        p_dist = diff/seq_len
        matrix[i, ii] = p_dist
        matrix[ii, i] = p_dist

np.savetxt('rosalind_pdst_result.txt', matrix, fmt='%.5f', delimiter=' ', newline='\n', header='', footer='', comments='# ', encoding=None)
