import matplotlib

from Pablos.matrix import *
from Pablos.stepresult import StepResult

matplotlib.use('TkAgg')
import math
import random

density = 0.8
threshold = 0.7
percent_unhappy = float('nan')
percent_similar = float('nan')

time = 0


def generate_initial_matrix(width, height):
    """
    Schelling's segregation model (1971)
    """
    matrix = Matrix.zero_matrix(width, height)

    deploy_agents(matrix)

    return StepResult(matrix, 0, 0)


def deploy_agents(matrix):
    empty_cells = matrix.get_empty_cells()

    desired_num_of_agents = get_desired_num_of_agents(density, matrix)

    for agent_id in range(desired_num_of_agents):
        cell = random.choice(empty_cells)
        cell.set_agent(Agent())
        empty_cells.remove(cell)

    not_colored_agents = matrix.get_agents()

    red_agents = random.sample(not_colored_agents, int(math.floor(len(not_colored_agents) / 2)))
    for agent in red_agents:
        agent.color = Colors.Red

    blue_agents = [x for x in not_colored_agents if x not in red_agents]
    for agent in blue_agents:
        agent.color = Colors.Blue


def get_desired_num_of_agents(density, matrix):
    width, height = matrix.get_size()
    return int(math.floor(density * (width * height)))
