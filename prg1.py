def fibonacci_series(n):
    series = []
    a, b = 1, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

if __name__ == "__main__":
    try:
        count = int(input("Enter the number of Fibonacci terms: "))
    except ValueError:
        print("Please enter a valid integer.")
    else:
        if count <= 0:
            print("Please enter a positive integer.")
        else:
            print("Fibonacci series:", * fibonacci_series(count))
