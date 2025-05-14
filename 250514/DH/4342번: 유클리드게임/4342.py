import sys

def game(a, b):
    turn = 0
    while True:
        if a < b:
            a, b = b, a
        if b == 0:
            return "A wins" if turn == 1 else "B wins"
        if a // b >= 2:
            return "A wins" if turn == 0 else "B wins"
        a, b = b, a % b
        turn ^= 1

for line in sys.stdin:
    a, b = map(int, line.split())
    if a == 0 and b == 0:
        break
    print(game(a, b))
