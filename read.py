import argparse


def read_file(input_file, mode="head", n_lines=5):
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            lines = file.readlines()

        if mode == "tail":
            lines_to_print = lines[-n_lines:]
        else:
            lines_to_print = lines[:n_lines]

        for line in lines_to_print:
            print(line.rstrip())
    except FileNotFoundError:
        print(f"Error file '{input_file}': not found")
    except Exception as e:
        print(f"Error reading '{input_file}': {e}")


# Create the parser
parser = argparse.ArgumentParser(
    description="Display first or last lines of a file", epilog="Best program ever"
)

parser.add_argument("-i", "--input", required=True, metavar="FILE", help="Input file")

parser.add_argument(
    "-v", "--verbose", help="increase verbosity", type=int, choices=[1, 2]
)


group = parser.add_mutually_exclusive_group()

group.add_argument("--head", action="store_true", help="Display the first lines")

group.add_argument("--tail", action="store_true", help="Display the last lines")

args_list = None
args = parser.parse_args(args_list)

if args.tail:
    mode = "tail"
else:
    mode = "head"

read_file(args.input, mode)
