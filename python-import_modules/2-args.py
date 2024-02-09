#!/usr/bin/python3

import sys

def main():
    args = sys.argv[1:]
    num_args = len(args)
    
    if num_args == 0:
        print("0 argumentos.")
    else:
        print(f"{num_args} {'argumento:' if num_args == 1 else 'argumentos:'}")
        for i, arg in enumerate(args, 1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    main()
