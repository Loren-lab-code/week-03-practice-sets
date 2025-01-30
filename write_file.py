with open("source.txt", "w") as source_file:
    source_file.write("Hello, World!")

with open("source.txt", "a") as source_file:
    source_file.write("\nThis is appended text.")

with open("source.txt", "r") as source_file:
    contents = source_file.read()

with open("destination.txt", "w") as destination_file:
    destination_file.write(contents)

print("File operations completed successfully.")