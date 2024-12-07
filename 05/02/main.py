import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() 
        result = func(*args, **kwargs) 
        end_time = time.time()  
        print(f"Execution time: {end_time - start_time:.5f} seconds")
        return result
    return wrapper


@time_it
def generate_even_numbers():
    return [num for num in range(100001) if num % 2 == 0]


even_numbers = generate_even_numbers()

print(f"Total even numbers: {len(even_numbers)}")
