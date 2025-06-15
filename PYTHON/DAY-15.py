import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"[⏳] Running '{func.__name__}'... Please wait.")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("-" * 40)
        print(f"[✅] Done! '{func.__name__}' took {end - start:.4f} seconds to run.")
        print("-" * 40)
        return result
    return wrapper

@timer_decorator
def sample_function():
    print("✨ Function logic runs here! Crunching some data... ✨")
    time.sleep(1)  # Simulating processing
    print("🛠️  Work done!")

sample_function()
