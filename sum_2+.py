import argparse

# Create the parser
parser = argparse.ArgumentParser(
    description="Sum numbers (at least 2 required)", epilog="Best program ever"
)

# Adding a positional argument 2 or more
parser.add_argument(
    "numbers", nargs="+", help="Numers to sum (at least 2 required)", type=int
)


# Adding a optional argument to the parser
parser.add_argument(
    "-v", "--verbose", help="increase verbosity", type=int, choices=[1, 2]
)

# Execute the parse_args() method
args = parser.parse_args()

# Compute the sum
if len(args.numbers) < 2:
    parser.error("Provide at least two numbers")


total = sum(args.numbers)


if args.verbose == 2:
    print(f"I compute sum of {', '.join(map(str, args.numbers))}:")
    print(total)
elif args.verbose == 1:
    print(" + ".join(map(str, args.numbers)), "=", total)
else:
    print(total)
