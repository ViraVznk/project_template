from app.io.input import *
from app.io.output import *

def main():
    test_inpt = input_text()
    test_read = read_file("data/input.txt")
    test_read_pandas = read_file_pandas("data/input1.csv")
    output_text(test_inpt)
    output_text(test_read)
    output_text(test_read_pandas)
    write_file("data/output.txt", test_inpt)
    write_file("data/output.txt", test_read)
    write_file_pandas("data/output1.csv", test_read_pandas)

    pass
if __name__ == '__main__':
    main()