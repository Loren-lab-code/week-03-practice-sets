filename = "example.txt"

content = """Hello, this is an example file.
It contains lines of text.
The purpose of this is to count the number of lines, words, and characters in this file."""

with open(filename, 'w') as file:
    file.write(content)

with open(filename, 'r') as file:
    lines = file.readlines()
    line_count = len(lines)
    file.seek(0)
    content = file.read()
    word_count = len(content.split())

    char_count = len(content)

print(f"Total number of lines: {line_count}")
print(f"Total number of words: {word_count}")
print(f"Total number of characters: {char_count}")