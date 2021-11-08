import math
import random

from figure import Figure


class Tetrahedron(Figure):

    def __init__(self):
        super().__init__()
        self.edge_length = 0

    def get_figure(self, data, i):
        self.density = data[i]
        self.edge_length = data[i + 1]

    def get_random_figure(self):
        self.density = random.randint(1, 100)
        self.edge_length = random.randint(1, 31)

    def write_figure_in_file(self, output):
        output.write("Tetrahedron: density = {},"
                     " edge length = {},"
                     " surface area = {}\n"
                     .format(self.density, self.edge_length, self.surface_area()))

    def surface_area(self):
        return math.sqrt(3)*float(self.edge_length)*float(self.edge_length)
