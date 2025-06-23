import argparse

def convert_temperature(temp, unit):
    if unit == "C":
        converted = (temp * 9/5) + 32
        return f"{temp}°C = {converted:.2f}°F"
    elif unit == "F":
        converted = (temp - 32) * 5/9
        return f"{temp}°F = {converted:.2f}°C"
    else:
        return "❌ Invalid unit. Please use 'C' or 'F'."

def main():
    parser = argparse.ArgumentParser(
        description="🌡️ Temperature Converter CLI Tool | Day 22 - #30DaysOfPython"
    )
    
    parser.add_argument(
        "--temp", 
        type=float, 
        required=True, 
        help="Temperature value to convert"
    )
    
    parser.add_argument(
        "--unit", 
        type=str, 
        choices=["C", "F"], 
        required=True, 
        help="Unit of the temperature (C for Celsius, F for Fahrenheit)"
    )

    args = parser.parse_args()
    
    result = convert_temperature(args.temp, args.unit)
    print(f"✅ Conversion Result: {result}")

if __name__ == "__main__":
    main()
