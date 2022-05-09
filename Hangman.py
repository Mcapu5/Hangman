import random
import os

def game(filepath = "./Hangman/datos.txt"):
    words = []
    with open (filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
    return words


def run():
    data = game(filepath="./Hangman/datos.txt")
    word = random.choice(data)
    word_list = [letter for letter in word]
    word_list_under = ["_"] * len(word_list)
    letter_dict = {}
    for idx, letter in enumerate(word):
        if not letter_dict.get(letter):
            letter_dict[letter] = []
        letter_dict[letter].append(idx)
    
    while True:
        os.system("cls")

        print("¡Adivina la palabra!")
        for element in word_list_under:
            print(element + " ", end="")
        print("\n")

        letter = input("Ingresa una letra: ").strip().upper()
        assert letter.isalpha(), "Solo puedes ingresar letras"

        if letter in word_list:
            for idx in letter_dict[letter]:
                word_list_under[idx] = letter
        
        if "_" not in word_list_under:
            os.system("cls")

            print("¡Ganaste! la palabra era ", word)
            break

if __name__ == "__main__":
    run()