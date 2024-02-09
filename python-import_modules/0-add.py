if __name__ == "__main__":
    import importlib
    add_module = importlib.import_module("0-add")
    add = add_module.add
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
