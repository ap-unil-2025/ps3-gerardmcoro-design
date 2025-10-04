"""
Problem 4: File Word Counter
Process text files and perform various analyses.
"""

import string

def create_sample_file(filename="sample.txt"):
    """
    Create a sample text file for testing.

    Args:
        filename (str): Name of the file to create
    """
    content = (
        "Python is a powerful programming language.\n"
        "It is widely used in web development, data science, and automation.\n"
        "Python's simple syntax makes it great for beginners.\n"
        "Many companies use Python for their projects."
    )

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {filename}")


def count_words(filename):
    """
    Count total words in the file.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        int: Total number of words
    """
    with open(filename, "r", encoding="utf-8") as f:
        return sum(len(line.split()) for line in f)


def count_lines(filename):
    """
    Count total lines in the file.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        int: Total number of lines
    """
    with open(filename, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def count_characters(filename, include_spaces=True):
    """
    Count characters in the file.

    Args:
        filename (str): Name of the file to analyze
        include_spaces (bool): Whether to include spaces in count

    Returns:
        int: Total number of characters
    """
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    if include_spaces:
        return len(text)
    else:
        # Quita todos los espacios en blanco (espacios, tabs, saltos de línea)
        # 'split' separa por cualquier whitespace y 'join' los pega sin separadores
        return len("".join(text.split()))


def _normalize_words(text):
    """
    Helper: quita signos de puntuación y devuelve lista de palabras en minúscula.
    """
    # Elimina puntuación con translate (más rápido que replace/regex para este caso)
    table = str.maketrans("", "", string.punctuation)
    cleaned = text.translate(table).lower()
    return cleaned.split()


def find_longest_word(filename):
    """
    Find and return the longest word in the file.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        str: The longest word found ('' si el archivo no tiene palabras)
    """
    with open(filename, "r", encoding="utf-8") as f:
        words = _normalize_words(f.read())

    if not words:
        return ""
    return max(words, key=len)


def word_frequency(filename):
    """
    Return a dictionary of word frequencies.
    Convert words to lowercase and remove punctuation.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        dict: {word: frequency}
    """
    with open(filename, "r", encoding="utf-8") as f:
        words = _normalize_words(f.read())

    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq


def analyze_file(filename):
    """
    Perform complete analysis of the file.

    Args:
        filename (str): Name of the file to analyze
    """
    print(f"\nAnalyzing: {filename}")
    print("-" * 40)

    try:
        # Display all analyses
        print(f"Lines: {count_lines(filename)}")
        print(f"Words: {count_words(filename)}")
        print(f"Characters (with spaces): {count_characters(filename, True)}")
        print(f"Characters (without spaces): {count_characters(filename, False)}")
        print(f"Longest word: {find_longest_word(filename)}")

        # Display top 5 most common words
        print("\nTop 5 most common words:")
        freq = word_frequency(filename)

        # Sort por frecuencia (desc) y luego alfabético (estable)
        top_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:5]
        for word, count in top_words:
            print(f"  '{word}': {count} times")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main function to run the file analyzer."""
    # Create sample file
    create_sample_file()

    # Analyze the sample file
    analyze_file("sample.txt")

    # Allow user to analyze their own file
    print("\n" + "=" * 40)
    user_file = input("Enter a filename to analyze (or press Enter to skip): ").strip()
    if user_file:
        analyze_file(user_file)


if __name__ == "__main__":
    main()
