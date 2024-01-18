#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *

    hidden = dir()
    for i in range(0, len(hidden)):
        if hidden[i][:2] != "__":
            print("{:s}".format(hidden[i]))
