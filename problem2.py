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

    # my attempt

    # define celsius variable

    fahrenheit = (celsius * 9 / 5) + 32

    return fahrenheit


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
    celsius = (fahrenheit - 32) * 5 / 9

    return celsius


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
        # TODO: Implement the interactive converter
        # Remember to:
        # - Get temperature value from user
        temperature = float(
            input(" entrez la température que vous souhaitez convertir:")
        )
        # - Get unit (C or F) from user
        unit = input(
            "Précisez quelle unité vous souhaitez convertir: C pour celsius ou F pour fahrenheit:"
        )
        # - Validate input
        if unit.upper() == "C":
            result = celsius_to_fahrenheit(temperature)
            print(f"{temperature}°C = {result:.2f}°F")
        elif unit.upper() == "F":
            result = fahrenheit_to_celsius(temperature)
            print(f"{temperature}°F = {result:.2f}°C")
        # - Perform conversion

        # - Display result rounded to 2 decimal places
        else:
            print("❌ Unité invalide. Utilisez 'C' ou 'F'.")
    except ValueError:
        print("❌ Veuillez entrer un nombre valide pour la température.")


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
