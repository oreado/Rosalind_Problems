f = open("rosalind_dna.txt", "r")
dna = f.read()
f.close()
res=open("rosalind_dna_result.txt","w")
res.writelines(" ".join(str(i) for i in counts))
res.close()