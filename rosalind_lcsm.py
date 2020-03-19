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

fa_list = fa2list('rosalind_lcsm.txt')
seqs = [x[1] for x in fa_list]
fragement = []
seq = seqs[0]

for from_pos in range(len(seq)):
    for to_pos in range(len(seq),from_pos,-1):
        fragement.append(seq[from_pos:to_pos])

fragement.sort(key=len, reverse=True)
fragement = [x for x in fragement if len(x)>1]

common_str = []
for x in fragement:
    count = 0
    for y in seqs:
        if (y.find(x) >= 0):
            count += 1
    if(count == len(seqs)):
        common_str.append(x)

print(common_str[0])