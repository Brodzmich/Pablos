from Pablos import matrixgenerator

import random

def run_algorithm(number_of_steps, width, height, vision):

    step_result = matrixgenerator.generate_initial_matrix(width, height)

    for i in range(1, number_of_steps + 1):
        step_result = perform_step(step_result, vision)

    return step_result

def perform_step(step_result, vision):
    global time

    time += 1
    percent_unhappy = 0
    percent_similar = 0.0

    matrix = step_result.matrix
    agents = list(matrix.get_agents())

    random.shuffle(agents)

    # for agent in agents:
    #     if agent_satisfied(agent)

    #     similar = 0
    #     total = 0
    #     for dx in range(-1, 2):  # promień sąsiedztwa!!
    #         for dy in range(-1, 2):
    #             if not ((dx == 0) and (dy == 0)):
    #                 v = step_result.matrix[(y + dy) % height, (x + dx) % width]
    #                 if (v != 0):
    #                     total += 1
    #                 if (v == state):
    #                     similar += 1
    #     if (total == 0):
    #         percent_similar += 1
    #     else:
    #         percent_similar += similar / (1.0 * total)
    #     if (similar < threshold * total):
    #         percent_unhappy += 1
    #         newpos = RD.randrange(len(step_result.empty))
    #         new_y, new_x = step_result.empty[newpos]
    #         step_result.matrix[new_y, new_x] = state
    #         step_result.agents[i] = step_result.empty[newpos]
    #         step_result.matrix[y, x] = 0
    #         step_result.empty[newpos] = agent
    # percent_unhappy /= (1.0 * len(step_result.agents))
    # percent_similar /= (1.0 * len(step_result.agents))

    # return StepResult(step_result.matrix, step_result.agents, step_result.empty, percent_unhappy, percent_similar)