from unittest import TestCase

import scipy as SP

from Pablos import matrixgenerator
from Pablos.colors import Colors
from Pablos.matrix import Matrix


class TestMatrixGenerator(TestCase):

    def test_agent_number_always_80_percent(self):
        matrix = Matrix.zero_matrix(10, 10)
        matrixgenerator.deploy_agents(matrix)

        self.assertEqual(80, len(matrix.get_agents()), "Number of agents should always be 80")

    def test_agent_colors_50_50(self):
        matrix = Matrix.zero_matrix(10, 10)

        matrixgenerator.deploy_agents(matrix)

        self.assertEqual(20, len(matrix.get_empty_cells()))
        agents = matrix.get_agents()

        red_agents = 0
        blue_agents = 0
        for agent in agents:
            if agent.color == Colors.Red:
                red_agents += 1
            elif agent.color == Colors.Blue:
                blue_agents += 1

        self.assertEqual(40, red_agents)
        self.assertEqual(40, blue_agents)

    def test_desired_number_of_agents(self):
        matrix = Matrix.zero_matrix(10, 10)
        desired_number = matrixgenerator.get_desired_num_of_agents(0.8, matrix)
        self.assertEqual(80, desired_number)

        matrix = Matrix.zero_matrix(3, 3)
        desired_number = matrixgenerator.get_desired_num_of_agents(0.8, matrix)
        self.assertEqual(7, desired_number)
