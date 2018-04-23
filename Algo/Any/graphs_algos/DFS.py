class Graph:
	def __init__(self):
		self.vertexes = []

	def add_vertex(self, v):
		self.vertexes.append(v)

class vertex:
	def __init__(self):
		self.adj = []
		self.d = None
		self.p = None
		self.color = 0 # 0 states to WHITE; 1 = GRAY; 2 = BLACK

def DFS(G):
	for u in G.vertexes:
		u.color = 0
		u.p = None
	for u in G.vertexes:
		if u.color == 0:
			DFS_visit(G, u)

def DFS_visit(G, u):
	u.color = 1
	for v in u.adj:
		if v.color == 0:
			v.p = u
			DFS_visit(G, v)
	u.color = 2



v_0 = vertex()
v_1 = vertex()
v_2 = vertex()
v_0.adj = [v_2]
v_1.adj = []
v_2.adj = [v_0, v_1]
G = Graph()
G.add_vertex(v_0)
G.add_vertex(v_1)
G.add_vertex(v_2)
DFS(G)
print(v_0.color)
print(v_1.color)
print(v_2.color)


