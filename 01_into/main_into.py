#1

fruits = ("banana", "apple", "mango", "strawberry", "orange", "apple", "mango")
name = input("Enter the name of a fruit: ").strip().lower()

count = sum(1 for fruit in fruits if fruit == name)
print(f"The fruit '{name}' appears {count} times in the tuple.")

#2
fruits = ("banana", "apple", "mango", "strawberry", "apple", "bananamango", "strawberry-banana")
name = input("Enter the name of a fruit: ").strip().lower()

count = sum(1 for fruit in fruits if name in fruit)
print(f"The fruit '{name}' appears {count} times (including as part of elements).")


#3
manufacturers = ("toyota", "ford", "bmw", "mercedes", "ford", "honda", "bmw")
name = input("Enter the manufacturer name to replace: ").strip().lower()
replacement_word = input("Enter the replacement word: ").strip()

updated = tuple(replacement_word if _ == name else _ for _ in manufacturers)
print("Updated tuple:", updated)


#4
nums = (1, 23, 456, 78, 9, 123, 4567, 89, 0, 12, 34, 567)
digit_stats = {}

for num in nums:
    digit_count = len(str(abs(num)))  
    digit_stats[digit_count] = digit_stats.get(digit_count, 0) + 1

for digits, count in sorted(digit_stats.items()):
    print(f"{digits} цифра{'и' if digits > 1 else ''} — {count} елемент{'ів' if count > 1 else ''}")
