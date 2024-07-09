"""
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
Input: 5
Output: 120
"""

n = 5
f = 1

while n > 1:
    f *= n
    n -= 1
print(f)


def func(n, f=1):
    if n == 1:
        return f
    return func(n - 1, f * n)

print(func(5))

if __name__ == "__main__":
    print(func(5))
