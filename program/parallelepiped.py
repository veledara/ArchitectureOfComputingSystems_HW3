import random

from figure import Figure


class Parallelepiped(Figure):

    def __init__(self):
        super().__init__()
        self.first_edge = 0
        self.second_edge = 0
        self.third_edge = 0

    def get_figure(self, data, i):
        self.density = data[i]
        self.first_edge = data[i + 1]
        self.second_edge = data[i + 2]
        self.third_edge = data[i + 3]

    def get_random_figure(self):
        self.density = random.randint(1, 100)
        self.first_edge = random.randint(1, 100)
        self.second_edge = random.randint(1, 100)
        self.third_edge = random.randint(1, 100)

    def write_figure_in_file(self, output):
        output.write("Parallelepiped: density = {},"
                     " first edge length = {},"
                     " second edge length = {},"
                     " third edge length = {},"
                     " surface area = {}\n"
                     .format(self.density, self.first_edge, self.second_edge, self.third_edge, self.surface_area()))

    def surface_area(self):
        return 2.0 * (float(self.first_edge) + float(self.second_edge) + float(self.third_edge))
