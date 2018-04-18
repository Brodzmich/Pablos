import matplotlib
from scipy import stats

from Pablos import stepresult
from Pablos.stepresult import StepResult

matplotlib.use('TkAgg')

import pylab as PL
import random as RD
import scipy as SP

RD.seed()

width = 12
height = 12
density = 0.8
threshold = 0.7
percent_unhappy = float('nan')
percent_similar = float('nan')


time = 0


def generate_initial_matrix():
    """
    Schelling's segregation model (1971)
    """

    agents = list()
    empty = list()

    matrix = SP.zeros([height, width])
    for x in range(width):
        for y in range(height):
            if RD.random() < density:
                agents.append((y, x))
                if RD.random() < 0.5:  # stosunek <0,5 czerwonych wiecej
                    matrix[y, x] = 1  # kolory
                else:
                    matrix[y, x] = -1
            else:
                empty.append((y, x))

    return StepResult(matrix, agents, empty, 0, 0)


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
