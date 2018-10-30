def repeat(nodes, der):
	global temp
	for i in nodes:
		if der == i[0]:
			temp.append(i[1])
			return repeat(nodes, i[1])
	return temp

for test in range(int(input())):
	A = []
	for c in range(int(input())):
		A.append(list(map(int, input().strip().split(' '))))
	nodes = []
	for i,v in enumerate(A):
		if v[0] != 0:
			for j in range(v[0]):
				nodes.append([i+1, v[j+1]])
	temp = []
	nodes.sort()
	
	tree = dict()
	for i in nodes:
		if i[0] in tree:
			if i[-1] not in tree[i[0]]:
				tree[i[0]].append(i[-1])
		else:
			tree[i[0]] = [i[-1]]

	l = len(nodes)
	count = 0
	for i,j in tree.items():
		if len(j) > 1:
			count += 1
		s = repeat(nodes[count:], j[0]+1)
		if s != []:
			nodes.append([1] + s)
	print(nodes)
	break
	flag = 'No'
	for i in nodes:
		for j in nodes[nodes.index(i)+1:]:
			if i[0] == j[0] and i[-1] == j[-1]:
				flag = True
	print("Case #{0}: {1}".format(test + 1, flag))