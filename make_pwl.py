import random

random.seed(0)


BIT_TIME_IN_NS = 2.08

DEFAULT_BIN_FILE_NAME = "data.txt"
DEFAULT_BIN_FILE_SIZE = 1024 * 64
DEFAULT_PWL_FILE_NAME = "data.pwl.txt"


def make_bin_data_file(data_filename=DEFAULT_BIN_FILE_NAME, size=DEFAULT_BIN_FILE_SIZE):
    """
    generate random sequence of bits
    output file will be by default data.txt
    """
    with open(data_filename, "w") as df:
        for _ in range(size):
            random_byte = str(int(random.random() * 2))
            df.write(random_byte)


def make_pwl_file(
    bin_filename=DEFAULT_BIN_FILE_NAME, pwl_filename=DEFAULT_PWL_FILE_NAME
):
    """
    make a PWL file from a binary file
    """
    # open the 'bin_filename' file for read
    # and write PWL data in an new file 'pwl_filename'
    with open(bin_filename) as bin_f, open(pwl_filename, "w") as pwl_f:
        time = 0
        while input_byte := bin_f.read(1):
            volts = 10 * 1e-3 if input_byte == "0" else 440 * 1e-3
            line = f"{time}ns{chr(9)}{volts}\n"
            pwl_f.write(line)
            time = time + BIT_TIME_IN_NS


make_bin_data_file()
make_pwl_file()
