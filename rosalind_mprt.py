import urllib.request
import re

def get_fasta(ID):
    url = 'http://www.uniprot.org/uniprot/'+ID+'.fasta'
    res = urllib.request.urlopen(url)
    fasta = [str(x)[2:-3] for x in res.readlines()][1:]
    return(''.join(fasta))

def find_motif(fasta):
    motif = re.compile(r'N[^P][ST][^P]')
    match_start = []
    start = -1
    while len(fasta) >= 4:
        found = motif.search(fasta)
        if(not found):
            break
        start = start + 1 + found.start()
        match_start.append(start)
        fasta = fasta[found.start()+1:]
    return(match_start)

with open('rosalind_mprt.txt', 'r') as f:
    IDs = [x.rstrip() for x in f.readlines()]

IDs_short = [x.split('_')[0] for x in IDs]

fastas = map(get_fasta, IDs_short)

starts = list(map(find_motif, fastas))

with open('rosalind_mprt_result.txt', 'w') as f1:
    for i in range(len(IDs)):
        if(starts[i]):
            print(IDs[i],'\n',' '.join([str(x) for x in starts[i]]))
            f1.write(IDs[i]+'\n'+' '.join([str(x) for x in starts[i]])+'\n')
