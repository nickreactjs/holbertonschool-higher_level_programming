#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print(sum(int(sys.argv[i]) for i in range(1, len(sys.argv))))
