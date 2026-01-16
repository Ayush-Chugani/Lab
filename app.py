# app.py
import sys

def area(r):
    return 3.14 * r * r

if __name__ == "__main__":
    radius = float(sys.argv[1])
    print(area(radius))