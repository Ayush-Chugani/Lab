# app.py
import sys

def area(r):
    return 3.14 * r * r

if __name__ == "__main__":
    print(area(float(sys.argv[1])))
