"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = []

    while True:
        # TODO: Get input from user
        # TODO: Check if user typed 'done'
        # TODO: Try to convert to float and add to list
        # TODO: Handle invalid input gracefully
        pass

    return numbers

def get_numbers_from_user():
    """
    Pide números hasta que el usuario escriba 'done' (o vacío).
    Devuelve la lista de números (floats).
    """
    numbers = []
    while True:
        raw = input("Enter a number (or 'done' to finish): ").strip()
        if raw.lower() in ("done", ""):
            break
        try:
            num = float(raw.replace(",", "."))  # acepta coma decimal
            numbers.append(num)
        except ValueError:
            print("Please enter a valid number or 'done'.")
    return numbers


def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:
        return None

    analysis = {}

    # TODO: Calculate count
    # TODO: Calculate sum
    # TODO: Calculate average
    # TODO: Find minimum
    # TODO: Find maximum
    # TODO: Count even numbers (hint: use modulo operator)
    # TODO: Count odd numbers

    return analysis

def analyze_numbers(numbers):
    """
    Devuelve métricas básicas sobre una lista de números.
    Si la lista está vacía, devuelve None.
    """
    if not numbers:
        return None

    count = len(numbers)
    total = sum(numbers)
    average = total / count
    minimum = min(numbers)
    maximum = max(numbers)

    even_count = sum(1 for x in numbers if x % 2 == 0)
    odd_count = count - even_count

    return {
        "count": count,
        "sum": total,
        "average": average,
        "minimum": minimum,
        "maximum": maximum,
        "even_count": even_count,
        "odd_count": odd_count,
    }


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        return

    print("\nAnalysis Results:")
    print("-" * 20)

    # TODO: Display all analysis results in a nice format
    # Example:
    # Count: 5
    # Sum: 25
    # Average: 5.00
    # etc.
    pass

def display_analysis(analysis):
    """Muestra el diccionario de métricas en formato legible."""
    if not analysis:
        print("No analysis to display.")
        return
    print("\nAnalysis Results:")
    print("-" * 20)
    print(f"Count:     {analysis['count']}")
    print(f"Sum:       {analysis['sum']}")
    print(f"Average:   {analysis['average']:.2f}")
    print(f"Minimum:   {analysis['minimum']}")
    print(f"Maximum:   {analysis['maximum']}")
    print(f"Evens:     {analysis['even_count']}")
    print(f"Odds:      {analysis['odd_count']}")

def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()
    
def main():
    """Ejecuta el analizador de números en modo interactivo."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    numbers = get_numbers_from_user()
    if not numbers:
        print("No numbers entered!")
        return

    analysis = analyze_numbers(numbers)
    display_analysis(analysis)
