import sys
import time
from container import Container

if __name__ == '__main__':
    begin_time = time.perf_counter()
    if len(sys.argv) != 5:
        print("Incorrect command line.\nPlease write: "
              "[python main] -f <input_file_name> <output_file_name> <output_sorted_file_name>\n"
              "Or: [python main] -n <number_of_figures> <output_file_name> <output_sorted_file_name>")
        exit()
    container = Container()
    if sys.argv[1] == "-f":
        input_file_name = open(sys.argv[2])
        input_string = input_file_name.read()
        data_array = input_string.replace("\n", " ").split(" ")
        container.file_input(data_array)
        input_file_name.close()
    elif sys.argv[1] == "-n":
        number_of_figures = int(sys.argv[2])
        if number_of_figures < 1 or number_of_figures > 10001:
            print("Incorrect number of figures. Number must be greater than or equal to 1 and less than 1001")
            exit()
        container.random_input(number_of_figures)
    else:
        print("Incorrect command line.\nPlease write: "
              "[python main] -f <input_file_name> <output_file_name> <output_sorted_file_name>\n"
              "Or: [python main] -n <number_of_figures> <output_file_name> <output_sorted_file_name>")
        exit()

    output_file = open(sys.argv[3], 'w')
    container.write_in_file(output_file)
    output_file.close()
    output_sorted_file = open(sys.argv[4], 'w')
    container.sort()
    container.write_in_file(output_sorted_file)
    output_sorted_file.close()
    end_time = time.perf_counter()
    print("Time: {}".format(end_time - begin_time))
