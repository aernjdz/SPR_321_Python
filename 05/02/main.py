# import time


# def time_it(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time() 
#         result = func(*args, **kwargs) 
#         end_time = time.time()  
#         print(f"Execution time: {end_time - start_time:.5f} seconds")
#         return result
#     return wrapper


# @time_it
# def generate_even_numbers():
#     return [num for num in range(100001) if num % 2 == 0]


# even_numbers = generate_even_numbers()

# print(f"Total even numbers: {len(even_numbers)}")


def fix_negative_params(func):
    def wrapper(*args, **kwargs):
      
        fixed_args = tuple(arg if not isinstance(arg, (int, float)) or arg >= 0 else 1 for arg in args)
        fixed_kwargs = {k: (v if not isinstance(v, (int, float)) or v >= 0 else 1) for k, v in kwargs.items()}
        return func(*fixed_args, **fixed_kwargs)
    return wrapper


@fix_negative_params
def main(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)


main(10, -3, "red", -1, 200, color="blue", size=-50)