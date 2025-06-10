try:
    # Trying to read a file line by line and convert to integers
    with open("numbers.txt", "r") as file:
        numbers = [int(line.strip()) for line in file]
    print("Sum:", sum(numbers))

except FileNotFoundError:
    print("Oops! The file doesn't exist. Check the name or path 🧐")

except ValueError:
    print("Error: File has some non-numeric data 😬")

finally:
    print("Process complete. ✅")