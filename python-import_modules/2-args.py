#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number_arg = len(sys.argv) - 1
    args_list = sys.argv[1:]

    if number_arg == 0:
        print(f"{number_arg} arguments.")
    elif number_arg == 1:
        print(f"{number_arg} argument:")
    else:
        print(f"{number_arg} arguments:")
    if number_arg:
        for i, arg in enumerate(args_list, 1):
            print(f"{i}: {arg}")
