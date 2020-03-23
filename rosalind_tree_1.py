def read_data(file):
    with open(file, 'r') as f:
        data = [x.rstrip() for x in f.readlines()]
    node_number = int(data.pop(0))
    adj_list = [x.split(' ') for x in data]
    return(node_number, adj_list)

def grouping(adj_list, groups):
    for i in range(1,len(adj_list)):
        node1 = adj_list[i][0]
        node2 = adj_list[i][1]
        node1_group = -1
        node2_group = -1
        for ii in range(len(groups)):
            group = groups[ii]
            if(node1 in group):
                node1_group = ii
            if(node2 in group):
                node2_group = ii
            if(node1_group>-1 and node2_group>-1):
                break
        if(node1_group>-1):
            if(node2_group==-1):
                groups[node1_group].append(node2)
            else:
                groups[node1_group] = groups[node1_group] + groups[node2_group]
                del(groups[node2_group])
        elif(node2_group>-1):
            groups[node2_group].append(node1)
        else:
            groups.append(adj_list[i])
    return(groups)

def main(file, n):
    node_number, adj_list = read_data(file)
    groups = []
    nodes_in_group = []
    groups.append(adj_list[0])
    nodes_in_group.append(adj_list[0][0])
    nodes_in_group.append(adj_list[0][1])
    for edge in adj_list:
        nodes_in_group.append(edge[0])
        nodes_in_group.append(edge[1])
    nodes_in_group = list(set(nodes_in_group))
    nodes_not_group = set([str(x) for x in range(node_number,0,-1)]).difference(nodes_in_group)
    grouping(adj_list, groups)
    n_groups = len(groups) + len(nodes_not_group)
    print(n_groups - 1)

if(__name__ == '__main__'):
    main('rosalind_tree.txt')