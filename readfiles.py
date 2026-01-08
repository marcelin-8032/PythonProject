import sys


def read_and_print_files(filenames):
    for filename in filenames:
        print(f"\n================{filename}================")
        try:
            with open(filename, "r", encoding="utf-8") as file:
                print(file.read())
        except FileNotFoundError:
            print(f"Error file '{filename}': not found")
        except Exception as e:
            print(f"Error reading '{filename}': {e}")


if len(sys.argv) < 2:
    print("Usage python readfiles.py <file1> <file2> ...")
    sys.exit(1)

filesnames = sys.argv[1:]
read_and_print_files(filesnames)
