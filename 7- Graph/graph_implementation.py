class Graph:

    def __init__(self):
        self.adj_list = {}

    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
            return True
        return False
    

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            try:
                self.adj_list[vertex1].remove(vertex2)
                self.adj_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False
    

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for related_vertex in self.adj_list[vertex]:
                self.adj_list[related_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
    

    def print_graph(self):
        for vertex in self.adj_list:
            print(f'{vertex} -> {self.adj_list[vertex]}')
        print('------------------------------')


if __name__ == '__main__':
    airports = ['IST', 'AMS', 'CDG', 'JFK']
    my_graph = Graph()

    for airport in airports:
        my_graph.add_vertex(vertex=airport)

    my_graph.add_edge(vertex1='IST', vertex2='AMS')
    my_graph.add_edge(vertex1='IST', vertex2='CDG')
    my_graph.add_edge(vertex1='IST', vertex2='JFK')
    my_graph.add_edge(vertex1='AMS', vertex2='CDG')
    my_graph.add_edge(vertex1='AMS', vertex2='JFK')
    my_graph.add_edge(vertex1='CDG', vertex2='JFK')

    my_graph.print_graph()

    my_graph.remove_edge(vertex1='IST', vertex2='JFK')

    my_graph.print_graph()

    my_graph.remove_vertex(vertex='AMS')

    my_graph.print_graph()