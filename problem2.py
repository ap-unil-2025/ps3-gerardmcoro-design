"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32

    Args:
        celsius (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit
    """
    # TODO: Implement this function
    return round(celsius*9/5+32, 2)


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) × 5/9

    Args:
        fahrenheit (float): Temperature in Fahrenheit

    Returns:
        float: Temperature in Celsius
    """
    # TODO: Implement this function
    return (round((fahrenheit-32)*5/9, 2))

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

    # TODO: Implement the interactive converter
    # Remember to:
    # - Get temperature value from user
    # - Get unit (C or F) from user
    # - Validate input
    # - Perform conversion
    # - Display result rounded to 2 decimal places
    
def temperature_converter():
    """Interactive temperature converter."""
    print("Temperature Converter")
    print("-" * 30)

    # 1) Pedir un número hasta que sea válido
    while True:
        raw = input("Enter the temperature value: ").strip()
        try:
            value = float(raw.replace(",", "."))
            break
        except ValueError:
            print("Please enter a numeric value (e.g., 36.6).")

    # 2) Pedir la unidad (C/F) hasta que sea válida
    while True:
        unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().lower()
        if unit in ("c", "f"):
            break
        print("Please type 'C' for Celsius or 'F' for Fahrenheit.")

    # 3) Convertir y mostrar
    if unit == "c":
        result = celsius_to_fahrenheit(value)
        print(f"{value:.2f}°C is {result:.2f}°F")
    else:
        result = fahrenheit_to_celsius(value)
        print(f"{value:.2f}°F is {result:.2f}°C")


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