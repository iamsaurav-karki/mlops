## Example 1: Temperature Conversion Function
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius


## Factorial Function
def factorial(n):
    """Return the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# Calling the functions
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C is {temp_f}°F")
temp_f2 = 77
temp_c2 = fahrenheit_to_celsius(temp_f2)
print(f"{temp_f2}°F is {temp_c2}°C")
fact_5 = factorial(5)
print(f"Factorial of 5 is {fact_5}")



# Example 2: Password Strength Checker
def is_strong_password(password):
    """Check if the password is strong."""
    if (len(password) >= 8 and
        any(char.isdigit() for char in password) and
        any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        any(char in "!@#$%^&*()-_+=" for char in password)):
        return True
    return False
# Testing the password strength checker
password = "StrongP@ssw0rd"
if is_strong_password(password):
    print("The password is strong.")
else:
    print("The password is weak.")

password2 = "weakpass"
if is_strong_password(password2):
    print("The password is strong.")
else:
    print("The password is weak.")


# Example 3: Total cost of items in a shopping cart
def calculate_total_cost(prices, tax_rate=0.07):
    """Calculate total cost including tax."""
    subtotal = sum(prices)
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total
# Testing the total cost calculation
item_prices = [19.99, 5.49, 3.50, 12.99]
total_cost = calculate_total_cost(item_prices)
print(f"Total cost including tax: ${total_cost:.2f}")
