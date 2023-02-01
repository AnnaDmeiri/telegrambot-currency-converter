numbers = ['0', '1', '2', '3']

with open("example.txt", "a") as file:
    for number in numbers:
        file.write(number + '\n')
