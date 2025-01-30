
with open("numbers.txt", "w") as file:
    for number in range(1, 11):  
        file.write(f"{number}\n") 

print("The numbers 1 to 10 has been written to 'numbers.txt'.")