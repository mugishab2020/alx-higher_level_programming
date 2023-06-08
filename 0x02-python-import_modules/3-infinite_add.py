#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = 0
    for a in range(len(sys.argv) - 1):
        number += int(sys.argv[a + 1])
    print("{}".format(number))
