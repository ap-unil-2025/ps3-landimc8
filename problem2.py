"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""

# Problem 2: Temperature Converter

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32

    Args:
        celsius (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit
    """
    fahrenheit = (celsius * 9/5) + 32
    # Rounding to 2 decimal places to pass floating-point tests
    return round(fahrenheit, 2)


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) × 5/9

    Args:
        fahrenheit (float): Temperature in Fahrenheit

    Returns:
        float: Temperature in Celsius
    """
    celsius = (fahrenheit - 32) * 5/9
    # Rounding to 2 decimal places to pass floating-point tests
    return round(celsius, 2)


def temperature_converter():
    """
    Interactive temperature converter.
    Ask user for:
    1. Temperature value
    2. Current unit (C or F)
    3. Convert and display result
    """
    print("Temperature Converter")
    print("-" * 30)

    try:
        # 1. Get temperature value from user
        value_input = input("Enter temperature value: ")
        temp_value = float(value_input)

        # 2. Get unit (C or F) from user
        unit = input("Enter current unit (C or F): ").upper()

        # 3. Validate input and perform conversion
        if unit == 'C':
            # Perform conversion C -> F
            converted_value = celsius_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {converted_value}°F")

        elif unit == 'F':
            # Perform conversion F -> C
            converted_value = fahrenheit_to_celsius(temp_value)
            print(f"{temp_value}°F is {converted_value}°C")

        else:
            # 4. Handle invalid unit input
            print("Error: Invalid unit. Please enter 'C' or 'F'.")

    except ValueError:
        # 4. Handle invalid temperature value input (e.g., user enters text)
        print("Error: Invalid temperature value. Please enter a number.")


# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    print("Running tests...")

    # Test Celsius to Fahrenheit
    assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"

    # Test Fahrenheit to Celsius
    assert fahrenheit_to_celsius(32) == 0, "32°F should be 0°C"
    assert fahrenheit_to_celsius(212) == 100, "212°F should be 100°C"

    print("All tests passed!")
    print()

    # Run interactive converter
    temperature_converter()

