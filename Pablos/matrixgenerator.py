import matplotlib

from Pablos.agent import Agent
from Pablos.colors import Colors
from Pablos.matrix import *
from Pablos.stepresult import StepResult

matplotlib.use('TkAgg')
import math
import random as RD

RD.seed()

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
        cell = RD.choice(empty_cells)
        cell.set_agent(Agent())
        empty_cells.remove(cell)

    not_colored_agents = matrix.get_agents()

    red_agents = RD.sample(not_colored_agents, int(math.floor(len(not_colored_agents) / 2)))
    for agent in red_agents:
        agent.color = Colors.Red

    blue_agents = [x for x in not_colored_agents if x not in red_agents]
    for agent in blue_agents:
        agent.color = Colors.Blue


def get_desired_num_of_agents(density, matrix):
    width, height = matrix.get_size()
    return int(math.floor(density * (width * height)))


def perform_step(step_result):
    global time

    time += 1
    percent_unhappy = 0
    percent_similar = 0.0

    height, width = step_result.matrix.shape

    sequence = list(range(len(step_result.agents)))
    RD.shuffle(sequence)
    for i in sequence:
        agent = step_result.agents[i]
        y, x = agent
        state = step_result.matrix[y, x]
        if state == 0:
            continue
        similar = 0
        total = 0
        for dx in range(-1, 2):  # promień sąsiedztwa!!
            for dy in range(-1, 2):
                if not ((dx == 0) and (dy == 0)):
                    v = step_result.matrix[(y + dy) % height, (x + dx) % width]
                    if (v != 0):
                        total += 1
                    if (v == state):
                        similar += 1
        if (total == 0):
            percent_similar += 1
        else:
            percent_similar += similar / (1.0 * total)
        if (similar < threshold * total):
            percent_unhappy += 1
            newpos = RD.randrange(len(step_result.empty))
            new_y, new_x = step_result.empty[newpos]
            step_result.matrix[new_y, new_x] = state
            step_result.agents[i] = step_result.empty[newpos]
            step_result.matrix[y, x] = 0
            step_result.empty[newpos] = agent
    percent_unhappy /= (1.0 * len(step_result.agents))
    percent_similar /= (1.0 * len(step_result.agents))

    return StepResult(step_result.matrix, step_result.agents, step_result.empty, percent_unhappy, percent_similar)
