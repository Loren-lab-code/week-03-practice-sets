import csv


def replace_word_in_file(input_file, old, new, output_file=None):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        updated_lines = [line.replace(old, new) for line in lines]
        if output_file is None:
            output_file = input_file  
        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(updated_lines)
        print(f"Replacement complete. Changes saved to '{output_file}'.")
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    replace_word_in_file()