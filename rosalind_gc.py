with open('rosalind_gc.txt', 'r') as f:
    fa = f.readlines()
fa = [x.replace('\n', '') for x in fa]

cut_line = []
names = []
seqs = []
gc_contents = []
max_index = 0

for i in range(len(fa)):
    txt = fa[i]
    if '>' in txt:
        cut_line.append(i)
        names.append(txt.replace('>', ''))
cut_line.append(len(fa)+1)

for ii in range(len(cut_line)-1):
    seq = fa[cut_line[ii]+1: cut_line[ii+1]]
    seq = ''.join(seq)
    gc_content = (seq.count('G')+seq.count('C'))*100/len(seq)
    seqs.append(seq)
    gc_contents.append(gc_content)
    if max(gc_contents) == gc_content:
        max_index = ii


result = names[max_index]+'\n'+format(gc_contents[max_index], '.6f')