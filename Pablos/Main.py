from Pablos import MatrixGenerator as matrix_generator

# start of the program
number_of_steps = 10
matrix = matrix_generator.generate_initial_matrix()

for i in range(number_of_steps):
    print("matrix ", i)
    print(matrix)
    matrix = matrix_generator.perform_step(matrix)
