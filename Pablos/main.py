from Pablos import matrixgenerator

# start of the program
number_of_steps = 10
step_result = matrixgenerator.generate_initial_matrix()

print("percent unhappy initial: ", step_result.percent_unhappy)
print("percent similar initial: ", step_result.percent_similar)

for i in range(1, number_of_steps + 1):
    step_result = matrixgenerator.perform_step(step_result)
    print("percent unhappy step {}: {} ".format(i, step_result.percent_unhappy))
    print("percent similar step {}: {}".format(i, step_result.percent_similar))
