file = 'rosalind_tree.txt'
def read_data(file):
    with open(file, 'r') as f:
        data = [x.rstrip() for x in f.readlines()]
    node_number = int(data.pop(0))
    adj_list = [x.split(' ') for x in data]
    return(node_number, adj_list)

node_number, adj_list = read_data(file)
print(node_number-1-len(adj_list))