from colorama import Fore, init
import random

def randWord():

    lines = open('wordle-answers-alphabetical.txt').read().splitlines()
    word = random.choice(lines)
    return word


def printResult(word, guess):
    if word == guess:
        raise
    for i in range(5):
        if guess[i] == word[i]:
            print(Fore.GREEN + guess[i], end='')
            a_list = list(word)
            a_list[i] = "*"
            word = ""
            word = "".join(a_list)
        elif guess[i] in word:
            print(Fore.YELLOW + guess[i], end='')
            a_list = list(word)
            a_list[word.find((guess[i]))] = "*"
            word = ""
            word = "".join(a_list)
        else:
            print(Fore.WHITE + guess[i], end='')
    print(Fore.WHITE)


def allowedGuess(s):
    with open('wordle-answers-alphabetical.txt') as f:
        if s in f.read():
            return True
    with open('wordle-allowed-guesses.txt') as f:
        if s in f.read():
            return True
    print('unallowed-guess')
    return False


def checkInput(s):
    if not s.isalpha():
        print("It's not all letters")
        return False
    if not len(s) == 5:
        print("It's not 5 letters")
        return False
    return True


def guess(word):
    while True:
        s = input("enter your guess")
        if checkInput(s) and allowedGuess(s):
            break
    printResult(word, s)

def main():
    word = randWord()
    print(word)
    try:
        for i in range(6):
            guess(word)
        print(Fore.RED + word)
        print(Fore.RED + "lose")
    except:
        print(Fore.GREEN + word)
        print(Fore.RED + "victory")


if __name__ == '__main__':
    main()
