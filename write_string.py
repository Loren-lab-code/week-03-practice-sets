strings_list = [
    "First line.",
    "Second line.",
    "Third line.",
    "Fourth line."
]

with open("output.txt", "w") as file:
    for string in strings_list:
        file.write(string + "\n") 

print("File 'output.txt' has been created with the list of strings.")