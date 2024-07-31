import sys

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments")
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

count = 0
try:
    with open(sys.argv[1]) as file:
        for line in file:
            if line.strip() != "" and not line.strip().startswith("#"):
                count += 1
    print(count)

except FileNotFoundError:
    sys.exit("File does not exist")