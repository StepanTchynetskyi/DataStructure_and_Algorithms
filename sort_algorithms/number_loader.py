def number_loader(path):
    with open(path, "r") as f:
        numbers = [int(line) for line in f]
    return numbers
