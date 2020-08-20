cube = lambda x: x**3

def fibonacci(n):
    fib_list = [0, 1]
    any(map(lambda _: fib_list.append(sum(fib_list[-2:])), range(2, n)))
    return fib_list[:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))