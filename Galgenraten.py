import random 

play = True

wordlist = ["Michael", "LeBron", "Kobe", "Shaquille", "Magic", "Larry", "Kareem", "Wilt", "Tim", "Stephen"]

index = random.randint(0,len(wordlist)-1)
right_letters = []
tries = 0

while play:
    print("_"*50)
    tries += 1
    i = 0
    j = 0
    word = wordlist[index]
    letter_s = input("Dein Buchstabe: ")
    right_letters.append(letter_s)
    guessed_correctly = False
    for letter_w in word:
        j += 1
        if letter_w in right_letters:
            print(letter_w, end=" ")
            guessed_correctly = True
            i += 1
        else:
            print('_', end=" ")
    print(f"                          Versuch: {tries}")
    if not guessed_correctly:
        right_letters.pop()
    if i == j:
        print()
        print(f"Du hast gewonnen und {tries} Versuche benötigt.")
        print("_"*50)
        play = False