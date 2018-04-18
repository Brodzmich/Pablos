from Pablos import matrixgenerator


def run_algorithm(number_of_steps, width, height):
    step_result = matrixgenerator.generate_initial_matrix(width, height)

    for i in range(1, number_of_steps + 1):
        step_result = matrixgenerator.perform_step(step_result)

    print("{} {}".format(step_result.percent_similar, step_result.percent_unhappy))
