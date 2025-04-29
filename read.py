file_name= "text.file"
length = int(input("enter the word length to find: "))

with open(file_name, "r") as file:
    word = file.read().split()
    for word in word:
        if len(word) == length:
            print(word)