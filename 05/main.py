import re
import json

users = {}

validators = {
    "length": lambda password: "Password must be at least 8 characters long." if len(password) < 8 else None,
    "uppercase": lambda password: "Password must include at least one uppercase letter." if not re.search(r"[A-Z]", password) else None,
    "lowercase": lambda password: "Password must include at least one lowercase letter." if not re.search(r"[a-z]", password) else None,
    "digit": lambda password: "Password must include at least one digit." if not re.search(r"\d", password) else None,
    "special": lambda password: "Password must include at least one special character." if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) else None
}

validate_password = lambda password: next(
    (error for validator in validators.values() if (error := validator(password))),
    None
)

def is_weak_password(password):
    return len(password) < 6 or password.isalpha()

commands = {
    "1": lambda username, password: (
        "User already exists." if username in users else 
        validate_password(password) or (users.update({username: password}) or "User added.")
    ),
    "2": lambda username: (
        "User not found." if username not in users else 
        (users.pop(username) or "User deleted.")
    ),
    "3": lambda username, new_password: (
        "User not found." if username not in users else 
        validate_password(new_password) or 
        ("New password must be different from the old one." if users[username] == new_password else 
        (users.update({username: new_password}) or "Password changed."))
    ),
    "4": lambda: "\n".join([f"{user}: {password}" for user, password in users.items()]) or "No users available.",
    "5": lambda: "\n".join([f"{user}: {password}" for user, password in users.items() if is_weak_password(password)]) or "No weak passwords found.",
    "6": lambda username: (
        f"Password for {username}: {users[username]}" if username in users else "User not found."
    ),
    "7": lambda file_name: (
        open(file_name, "w").write(json.dumps(users)) or f"User list saved to {file_name}."
    )
}

def handle_choice(choice):
    actions = {
        "1": lambda: (print(commands["1"](input("Enter username: "), input("Enter password: "))), True)[1],
        "2": lambda: (print(commands["2"](input("Enter username: "))), True)[1],
        "3": lambda: (print(commands["3"](input("Enter username: "), input("Enter new password: "))), True)[1],
        "4": lambda: (print("User list and passwords:\n" + commands["4"]()), True)[1],
        "5": lambda: (print("Weak passwords:\n" + commands["5"]()), True)[1],
        "6": lambda: (print(commands["6"](input("Enter username: "))), True)[1],
        "7": lambda: (print(commands["7"](input("Enter file name to save (e.g., users.json): "))), True)[1],
        "8": lambda: False  
    }
    return actions.get(choice, lambda: (print("Invalid choice. Try again."), True)[1])()

running = True
while running:
    print("\nMenu:")
    print("1. Add user")
    print("2. Delete user")
    print("3. Change password")
    print("4. View users and passwords")
    print("5. Check weak passwords")
    print("6. Get password by username")
    print("7. Save users to file")
    print("8. Exit")
    
    choice = input("Select an option (1-8): ")
    running = handle_choice(choice)
