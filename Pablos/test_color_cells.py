from unittest import TestCase

from Pablos import matrixgenerator

import scipy as SP


class TestMatrixGenerator(TestCase):

    def test_agent_number_always_80_percent(self):
        height = 10
        width = 10
        matrix = SP.zeros([height, width])
        agents = list()
        matrixgenerator.color_cells(matrix, height, width, agents, list())

        self.assertEqual(80, len(agents), "Number of agents should always be 80")

    def test_agent_colors_50_50(self):
        height = 10
        width = 10
        matrix = SP.zeros([height, width])
        agents = list()
        matrixgenerator.color_cells(matrix, height, width, agents, list())

        red_squares = 0
        blue_squares = 0

        for x in range(width):
            for y in range(height):
                color = matrix[x, y]
                if color == 1:
                    red_squares += 1
                elif color == -1:
                    blue_squares += 1

        self.assertEqual(40, red_squares)
        self.assertEqual(40, blue_squares)
