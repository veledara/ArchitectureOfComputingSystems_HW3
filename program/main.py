import sys
from container import Container

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Incorrect command line!\nYou must write: "
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
        if number_of_figures < 1 or number_of_figures > 1000:
            print("Incorrect number of figures. Number must be greater than or equal to 1 and less than 1001")
            exit()
        container.random_input(number_of_figures)
    else:
        print("Incorrect command line!\nYou must write: "
              "[python main] -f <inputFileName> <outputFileName> <outputSortedFileName>\n"
              "Or: [python main] -n <numberOfFigures> <outputFileName> <outputSortedFileName>")
        exit()

    output_file = open(sys.argv[3], 'w')
    container.write_in_file(output_file)
    output_sorted_file = open(sys.argv[4], 'w')
    container.sort()
    container.write_in_file(output_sorted_file)
