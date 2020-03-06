def count_hamm(seq1, seq2):
    hamm = 0
    for x1,x2 in zip(seq1, seq2):
        if x1 != x2:
            hamm += 1
    return(hamm)
if __name__ == '__main__':
    with open('rosalind_hamm.txt', 'r') as f:
        dnas = f.readlines()
    dnas = [x.rstrip() for x in dnas]
    count_hamm(dnas[0], dnas[1])