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
