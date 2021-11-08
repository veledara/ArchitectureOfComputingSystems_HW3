import random

from ball import Ball
from parallelepiped import Parallelepiped
from tetrahedron import Tetrahedron


class Container:
    def __init__(self):
        self.store = []

    def write_in_file(self, output):
        output.write("Container is store {} figures:\n".format(len(self.store)))
        for figure in self.store:
            figure.write_figure_in_file(output)
        output.write("Average surface area = {}\n".format(self.average_surface_area()))

    def sort(self):
        avg_surface_area = self.average_surface_area()
        for i in range(len(self.store)):
            if self.store[i].surface_area() > avg_surface_area:
                self.store.insert(0, self.store.pop(i))

    def average_surface_area(self):
        surface_area_sum = 0.0
        for figure in self.store:
            surface_area_sum += figure.surface_area()
        return surface_area_sum / len(self.store)

    def file_input(self, data):
        i = 0
        figure = None
        while i < len(data):
            figure_type = int(data[i])
            if figure_type == 1:
                figure = Ball()
                figure.get_figure(data, i + 1)
                i += 1
            elif figure_type == 2:
                figure = Parallelepiped()
                figure.get_figure(data, i + 1)
                i += 3
            elif figure_type == 3:
                figure = Tetrahedron()
                figure.get_figure(data, i + 1)
                i += 1
            i += 2
            self.store.append(figure)

    def random_input(self, number_of_figures):
        i = 0
        figure = None
        while i < number_of_figures:
            figure_type = random.randint(1, 3)
            if figure_type == 1:
                figure = Ball()
                figure.get_random_figure()
            elif figure_type == 2:
                figure = Parallelepiped()
                figure.get_random_figure()
            elif figure_type == 3:
                figure = Tetrahedron()
                figure.get_random_figure()
            i += 1
            self.store.append(figure)
