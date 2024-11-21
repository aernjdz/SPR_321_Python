#N1

n = int(input("Enter a number: "))
solve = {True: lambda x: f"{x} Even number", False: lambda x: f"{x} Odd number"}
print(solve[n % 2 == 0](n))


#N2

n = int(input("Enter a number: "))
solve = lambda x: f"{x} Number is a multiple of 7" if x % 7 == 0 else f"{x} Number is not a multiple of 7"
print(solve(n))

#N3 

num1, num2 = map(int, input("Enter two numbers separated by space: ").split())
find_max = lambda x, y: x if x > y else y
print(f"The maximum number is {find_max(num1, num2)}")


#4
num1, num2 = map(int, input("Enter two numbers separated by space: ").split())
find_min = lambda x, y: x if x < y else y
print(f"The minimum number is {find_min(num1, num2)}")

#5
num1, num2 = map(float, input("Enter two numbers separated by space: ").split())
operation = input("Choose an operation (sum, diff, avg, mult): ").strip().lower()

operations = {
    "sum": lambda x, y: x + y,
    "diff": lambda x, y: x - y,
    "avg": lambda x, y: (x + y) / 2,
    "mult": lambda x, y: x * y
}

result = operations.get(operation, lambda x, y: "Invalid operation")(num1, num2)
print(f"Result: {result}")

