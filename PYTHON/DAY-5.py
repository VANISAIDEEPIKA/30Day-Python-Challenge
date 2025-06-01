# ------------------------------------------
# 🧮 SUM & AVERAGE FUNCTION (Normal Function)
# ------------------------------------------

def compute_sum_and_average(numbers):
    # calculating the total sum using built-in sum()
    total = sum(numbers)
    
    # avoid divide-by-zero error
    if len(numbers) > 0:
        average = total / len(numbers)
    else:
        average = 0
    
    # returning both total and average
    return total, average

# 📌 Sample list
nums = [10, 20, 30, 40, 50]

# ✅ calling the function
total, avg = compute_sum_and_average(nums)

# 🖨️ displaying results
print("✅ Normal Function Results:")
print("Sum:", total)
print("Average:", avg)

# ------------------------------------------
# ⚡ LAMBDA VERSION (One-liner function)
# ------------------------------------------

# using lambda to do the same thing in one line
compute_lambda = lambda nums: (sum(nums), sum(nums) / len(nums) if len(nums) > 0 else 0)

# ✅ test it on another list
lambda_result = compute_lambda([5, 10, 15])

print("\n⚡ Lambda Function Results:")
print("Sum:", lambda_result[0])
print("Average:", lambda_result[1])

# ------------------------------------------
# 🔥 BONUS FUNCTION: MIN, MAX & RANGE
# ------------------------------------------

def compute_min_max_range(numbers):
    # handle empty list case
    if len(numbers) == 0:
        return None, None, None
    
    # using built-in functions
    minimum = min(numbers)
    maximum = max(numbers)
    value_range = maximum - minimum

    return minimum, maximum, value_range

# 📌 Sample data
nums2 = [12, 99, 43, 7, 65]

# ✅ call the function
min_val, max_val, range_val = compute_min_max_range(nums2)

print("\n🔥 Min, Max & Range Results:")
print("Minimum:", min_val)
print("Maximum:", max_val)
print("Range:", range_val)
