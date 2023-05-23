def fibonacci(n):
    if n <= 0:
        return "Invalid input! Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = [0, 1]
        for i in range(2, n):
            next_fib = fib_list[i-1] + fib_list[i-2]
            fib_list.append(next_fib)
        return fib_list

# Example usage:
print(fibonacci(10)) # prints [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]