import csv
import numpy as np

with open('{path}/junction.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    column_index = 1 #The index of the column which needs to be extracted
    column_data = [int(row[column_index]) for row in csvreader]


paid_edges =[]

with open('{path}/conduit.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skipping the Header

    # Reading the stored data from columns 3 and 5
    for row in csvreader:
      data_from_col_2 = int(row[2])
      if(row[4] == 'OF-2'):
        data_from_col_4 = int(0)
      else:
        data_from_col_4 = int(row[4])
      pair = (data_from_col_2, data_from_col_4)
      paid_edges.append(pair)


class Vertex:
	def __init__(self, n):
		self.name = n

class Graph:
	vertices = {}
	edges = []
	edge_indices = {}
	col_csv = [' ']
	row_csv = []
	final_csv = []


	def add_vertex(self, vertex):

		if isinstance(vertex, (Vertex, int)) and vertex not in self.vertices:
			if isinstance(vertex, int):
				vertex = Vertex(vertex)
			self.vertices[vertex.name] = vertex
			for row in self.edges:
				row.append(0)
			self.edges.append([0] * (len(self.edges)+1))

			self.edge_indices[vertex.name] = len(self.edge_indices)
			return True
		else:
			return False

	def add_edge(self, u, v, weight=1):
		if u in self.vertices and v in self.vertices:
			self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
			self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
			return True
		else:
			return False

	def print_graph(self):
		print('     '*10)
		for k in self.vertices:
			print(' ',k,end=' ' )
			self.col_csv.append(str(k))
		print("\n")

		for v, i in sorted(self.edge_indices.items()):
			print(v , end='')
			self.row_csv.append(str(v))
			for j in range(len(self.edges)):
				print(' '*8,self.edges[i][j], end=' ')
				self.row_csv.append(str(self.edges[i][j]))
			k = i +1
			print(' ')
			self.final_csv.insert(k, self.row_csv)
			self.row_csv = []

		self.final_csv.insert(0,self.col_csv)
		np.savetxt("AdjMatrix_pipemanholes.csv", self.final_csv ,delimiter = ", ", fmt ='%s')


g = Graph()

for i in column_data:
    g.add_vertex((i))


for pair in paid_edges:
	g.add_edge(pair[0],pair[1])

g.print_graph()



