from Pablos import algorithmrunner
from Pablos.filewriter import FileWriter

import time

# main file

file_writer = FileWriter("results-{}.txt".format(time.strftime("%Y%m%d%H%M%S")))

file_writer.write("simmilar          unhappy\n")

for i in range(5):
    result = algorithmrunner.run_algorithm(20, 50, 50, 1)
    file_writer.write("{} {}\n".format(result.percent_similar, result.percent_unhappy))

