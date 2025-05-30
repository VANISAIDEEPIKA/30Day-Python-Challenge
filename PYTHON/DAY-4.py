# Check if a user-entered number is a prime number 💡

# Step 1: Get input from the user (string to integer conversion)
num = int(input("Enter a number to check if it's prime: "))   # Type Conversion + Input

# Step 2: Handle edge cases first!
if num <= 1:                                                  # IF-ELSE: Check non-prime conditions
    print("❌ Not a prime number (Prime numbers are greater than 1)")
else:
    # Step 3: Assume it's prime unless we find a factor
    is_prime = True                                           # BOOLEAN FLAG

    # Step 4: Loop to check for factors (from 2 to num-1)
    for i in range(2, num):
        if num % i == 0:                                      # IF: Found a factor
            is_prime = False
            print(f"❌ Not a prime number. Divisible by {i}")  # BREAKING CONDITION
            break                                             #  BREAK stops the loop early

        else:
            continue  # CONTINUE isn't necessary here but shows we skip to next loop iteration

    # Step 5: If no factors were found
    if is_prime:                                              # FINAL CHECK
        print("✅ It's a prime number!")
