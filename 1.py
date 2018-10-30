from sys import stdin
 
# create directed graph
def build_graph(rawData):
    """ Graph is built into an adjacency list
    e.g. 2 3
         1 
    means that the first node points to the 2nd and 3rd and
    the second node points to the first with the 3rd node
    having no outgoing edges
    """
    graph={}
 
    count = 1
    for line in rawData:
        data = line.split()
        edges = []
        for edgesString in range(1, len(data)):
            edges.append(int(data[edgesString]))
        graph[count] = edges
        count+=1
 
    return graph
 
# count number of paths using BFS
""" The special trick: if the node currently exists in the path then
we can simply say that there is another path to this node and hence
break the loop as we have found there is more than 1 path to the target 
"""
def count_paths(graph, start, path=[]):
    numPaths=1
    q=[start]
    while q:
        v=q.pop(0)
        if not v in path:
            path=path+[v]
            q=q+graph[v]
        else:
            numPaths+=1
            break
    return numPaths
 
for i in range(int(stdin.readline())):
    rawData = []
    for node in range(int(stdin.readline())):
        rawData.append(stdin.readline())
    graph = build_graph(rawData)
 
    numPaths = 0
    # loop through all nodes in the graph
    for node in range(1,len(rawData)+1):
        numPaths = count_paths(graph, node)
        if numPaths >= 2: break
    isDiamond = 'Yes' if numPaths >= 2 else 'No'
    print('Case #'+str(i+1)+': ' + isDiamond)