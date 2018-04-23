class Queue:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []
	
	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

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

def BFS(G, start):
	Q = Queue()
	for u in G.vertexes:
		u.d = 999999
		u.p = None
	start.color = 1
	start.d = 0
	Q.enqueue(start)
	while not (Q.isEmpty()):
		u = Q.dequeue()
		for v in u.adj:
			if v.color == 0:
				v.color = 1
				v.d = u.d + 1
				v.p = u
				Q.enqueue(v)
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
BFS(G, v_0)
print(v_0.color)
print(v_1.color)
print(v_2.color)








