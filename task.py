# Task

# You are tasked with creating a Python program that serves as an interactive tool for a friend who enjoys exploring numbers. The program should begin by prompting the user to enter their name and then ask them for three of their favorite numbers. After gathering this information, 
# the program should greet the user with a personalized message that includes their name.
#  The three numbers provided by the user should be stored in a list.
#  The program should then check if any of the numbers are even or odd, and store this information in a separate list of tuples, where each tuple contains the number and a string indicating whether it is "even" or "odd". Following this, the program should use a for loop to iterate over the list of numbers, and for each number, 
# it should create a tuple containing the number and its square. These tuples should be printed in a creative and engaging format. Additionally, the program should calculate the sum of the three numbers and print the result, accompanied by an encouraging message. Finally, the program should determine if the sum is a prime number and notify the user with an appropriate message. The goal is to make the tool both enjoyable and informative, allowing the user to explore their favorite numbers in a fun and interactive way, while also introducing some interesting logical checks.

def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    # Get user information
    name = input("Hello! What's your name? ")
    print(f"Nice to meet you, {name}!")
    
    # Get favorite numbers
    numbers = []
    for i in range(3):
        number = int(input(f"Enter favorite number {i + 1}: "))
        numbers.append(number)
    
    # Determine if numbers are even or odd
    even_odd_info = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]
    
    # Print even/odd information
    print("\nHere is the list of your numbers and whether they are even or odd:")
    for num, ev_od in even_odd_info:
        print(f"Number {num} is {ev_od}.")
    
    # Create a list of tuples with number and its square
    squared_numbers = [(num, num ** 2) for num in numbers]
    
    # Print number and its square
    print("\nHere is each number and its square:")
    for num, square in squared_numbers:
        print(f"Number {num} squared is {square}.")
    
    # Calculate the sum of the numbers
    total_sum = sum(numbers)
    
    # Print the sum with an encouraging message
    print(f"\nThe sum of your numbers is {total_sum}. That's great!")
    
    # Check if the sum is a prime number
    if is_prime(total_sum):
        print("And guess what? The sum is a prime number!")
    else:
        print("The sum is not a prime number, but it's still awesome!")

if __name__ == "__main__":
    main()
