import pandas as pd
with open('rosalind_cons.txt', 'r') as f:
    fa = f.read().split('>')
del(fa[0])
fa = [x.rstrip() for x in fa]
fa_list = [x.split('\n') for x in fa]
for i in range(len(fa_list)):
    fa_list[i][1] = ''.join(fa_list[i][1:])
    del(fa_list[i][2:])
symbols = [list(x[1]) for x in fa_list]
symbols_table = pd.DataFrame(data = symbols)
profile = []
for N in ['A', 'C', 'G', 'T']:
    profile_N = [list(symbols_table.iloc[:,i]).count(N) for i in range(symbols_table.shape[1])]
    profile_N_str = ' '.join([str(x) for x in profile_N])
    profile.append(N + ': ' + profile_N_str)
profile = '\n'.join(profile)
consensus = [symbols_table.iloc[:,i].value_counts().index[0] for i in range(symbols_table.shape[1])]
consensus = ''.join(consensus)
result = consensus + '\n' + profile
with open('rosalind_cons_result.txt', 'w') as f1:
    f1.write(result)