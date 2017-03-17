##### 20170314 ######
# hw0b_movie
import csv
import networkx as nx

movie_nodes = open('C:/Python/project/data/hw0b/movie_nodes.txt', 'r', encoding = 'utf8')
dictNodes = dict([row for row in csv.reader(movie_nodes, delimiter = '\t')])

movie_edges = nx.read_weighted_edgelist('C:/Python/project/data/hw0b/movie_edgesW.txt', nodetype = int, delimiter = '\t')


N, K = movie_edges.order(), movie_edges.size()

# print(movie_edges[795])

## Ex. myDijkstra(movie_edges, 'Angelina Jolie', 'Megan Fox')
# Graph 網路
# start 起點
# end 終點
def myDijkstra(Graph, start, end):
	start = [int(k) for k, v in dictNodes.items() if v == start][0]
	end = [int(k) for k, v in dictNodes.items() if v == end][0]

	nodes = Graph.nodes() # 27312
	distance = dict(list(zip(nodes, [float('inf')] * len(nodes))))
	predecessor = dict(list(zip(nodes, [int(-1)] * len(nodes))))

	distance[start] = 0
	unvisited = nodes

	dijkstraL = []

	while len(unvisited) != 0:
		smallest = min({k: distance[k] for k in unvisited}, key = {k: distance[k] for k in unvisited}.get) # 6479
		if distance[smallest] == float('inf'):
			break
		if smallest == end:
			break
		unvisited.remove(smallest)
		currentDistance = distance[smallest]

		neighborS = Graph.neighbors(smallest)

		for k in range(len(neighborS)):
			newPath = currentDistance + list(Graph[smallest][neighborS[k]].values())[0]

			if newPath < distance[neighborS[k]]:
				distance[neighborS[k]] = newPath
				predecessor[neighborS[k]] = smallest
			D = {'node': neighborS[k], 'cost': distance[neighborS[k]], 'parent': predecessor[neighborS[k]]}
			dijkstraL.append(D)
	dijkstraL = [dict(y) for y in set(tuple(x.items()) for x in dijkstraL)] # 移除重複的紀錄

	aa = [x['node'] for x in dijkstraL] # 叫出所有的點

	bb = [k for k, x in enumerate(aa) if x == end] # 叫出所有等於終點的index
	cc = [dijkstraL[k] for k in bb] # 所有node等於終點的集合

	EndCost = min([x['cost'] for x in cc])

	S = []
	while predecessor[end] != int(-1):
		S.insert(0, end)
		# S.append(end)
		end = predecessor[end]
	S.insert(0, end)

	S = [dictNodes[str(j)] for j in S]
	
	return EndCost, S
	# return S
	print(EndCost)
	print(S)
	


RecordL = []

SearchL = [('Emma Watson', 'Leonardo DiCaprio'), ('Tom Cruise', 'Jennifer Lawrence'), ('Emma Watson', 'Johnny Depp'), ('Arnold Schwarzenegger', 'Meg Ryan'), ('Angelina Jolie', 'Megan Fox')]
# SearchL = [('Tom Cruise', 'Jennifer Lawrence')]

[RecordL.append(myDijkstra(movie_edges, j[0], j[1])) for j in SearchL]

print(RecordL)

# 把檔案寫出去
# myfile = open('C:/Python/project/data/hw0b/movieShortestPath.txt', 'w')

# # for item in RecordL:
# myfile.write('\n'.join('%s %s' % x for x in RecordL))
# myfile.close()


