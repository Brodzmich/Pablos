import random

from Pablos import matrixgenerator


def run_algorithm(number_of_steps, width, height, vision=1, threshold=0.5):
    step_result = matrixgenerator.generate_initial_matrix(width, height)

    for i in range(1, number_of_steps + 1):
        step_result = perform_step(step_result.matrix, vision, threshold)

    return step_result


def get_neighbors_of_agent(matrix, agent, vision):
    neighbors = list()
    for dx in range(0 - vision, vision + 1):
        for dy in range(0 - vision, vision + 1):
            if not ((dx == 0) and (dy == 0)):
                width, height = matrix.get_size()
                neighbors.append(matrix.cells[(agent.x + dx) % width][(agent.y + dy) % height])
    return neighbors


def agent_satisfied(matrix, agent, vison, threshold):
   neighbors = get_neighbors_of_agent(matrix, agent, vison)



def perform_step(matrix, vision, threshold):
    agents = list(matrix.get_agents())

    random.shuffle(agents)

    for agent in agents:
        agent_satisfied(matrix, agent, vision, threshold)

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
