import math
import random

from figure import Figure


class Ball(Figure):

    def __init__(self):
        super().__init__()
        self.radius = 0

    def get_figure(self, data, i):
        self.density = float(data[i])
        self.radius = data[i+1]

    def get_random_figure(self):
        self.density = float(random.randint(1, 100))+random.random()
        self.radius = random.randint(1, 20)

    def write_figure_in_file(self, output):
        output.write("Ball: density = {},"
                     " radius = {},"
                     " surface area = {}\n"
                     .format(self.density, self.radius, self.surface_area()))

    def surface_area(self):
        return 4.0 * math.pi * float(self.radius) * float(self.radius)
