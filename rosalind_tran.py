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


seq1 = fa2list('rosalind_tran.txt')[0][1]
seq2 = fa2list('rosalind_tran.txt')[1][1]

seq_match = zip(seq1, seq2)
dif_seq_match = [[x,y] for x,y in seq_match if x != y]

for i in range(len(dif_seq_match)):
    if(dif_seq_match[i][0] in ['A', 'G']):
        dif_seq_match[i][0] = 'pu'
    else:
        dif_seq_match[i][0] = 'py'
        
    if(dif_seq_match[i][1] in ['A', 'G']):
        dif_seq_match[i][1] = 'pu'
    else:
        dif_seq_match[i][1] = 'py'

Ti = len([x for x, y in dif_seq_match if x == y])
Tv = len([x for x, y in dif_seq_match if x != y])
print('%.11f'% (Ti/Tv))