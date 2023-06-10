import random

def read_word_from_file(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]

def read_hangman_from_file(file_path):
    with open(file_path, "r") as file:
        return file.read().split("\n\n")

words = read_word_from_file(r"C:\Users\HP\Downloads\words.txt")
hangman_stages = read_hangman_from_file(r"C:\Users\HP\Downloads\hangman.txt")
attempts = -1
random_word = random.choice(words)
word_length = "_ " * len(random_word)
missing_letters = list(word_length)
print(word_length)


while True:
    guess = input("Guess a letter: ")
    if guess in random_word:
        for i in range(len(random_word)):
            if random_word[i] == guess:
                missing_letters[i*2] = guess
        update = "".join(missing_letters)
        print(update)
        if "".join(missing_letters).replace(" ", "") == random_word:
            print("You won!")
            break
    else:
        attempts += 1
        print(hangman_stages[attempts])
    if attempts == 6:
        print("Sorry you lost, the word was", random_word + ".")
        break
