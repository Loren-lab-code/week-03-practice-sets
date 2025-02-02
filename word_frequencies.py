import csv
from collections import Counter

def count_word_frequency(example_file="example.txt", results_file="out.txt"):
    try:
        with open(example_file, 'r', encoding='utf-8') as file:
            text = file.read()
        words = text.split()
        word_count = Counter(words)
        with open(results_file, 'w', encoding='utf-8') as file:
            for word, count in word_count.items():
                file.write(f"{word}: {count}\n")
        print(f"Word frequency count saved to '{results_file}'.")
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

count_word_frequency