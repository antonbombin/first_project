s = 17
p = 72
for x in range(s):
    for y in range(p):
        if s == x + y and p == x * y and x <= y:
            print(f'{x} {y}')