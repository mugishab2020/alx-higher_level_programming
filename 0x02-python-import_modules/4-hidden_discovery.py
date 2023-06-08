#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    mn = dir(hidden_4)
    for name in mn:
        if name[:2] != "__":
            print(name)
