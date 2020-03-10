with open('rosalind_subs.txt', 'r') as f:
    s, t = [x.rstrip() for x in f.readlines()]
pos_list = []
i = 0
while i > -1:
    pos = s.find(t, i ,len(s))
    if(pos<0):
        i = pos
    else:
        pos_list.append(pos+1)
        i = pos+1
print(' '.join([str(x) for x in pos_list]))