#Generate a Fibonacci series up to n terms
fibonacci_series = lambda n: (
    lambda z: [z.append(z[-1] + z[-2]) for _ in range(n - 2)] and z
)([0, 1]) if n > 1 else [0][:n]
print(fibonacci_series(10))
