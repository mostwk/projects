def find_position(word, char):
    return [position for position, i in enumerate(word) if i == char]


def make_dictionary(char, list_of_positions):
    d = dict()
    d[char] = list_of_positions
    return d


def printing(dic, masked_word):
    for k in dic:
        for v in dic[k]:
            masked_word[v] = k
    return masked_word


def game(secret_word):
    tries = 0
    lives = 199
    hidden_word = ['*' for i in secret_word]
    while lives >= 0:
        print("Your word is: ", hidden_word)
        if '*' in hidden_word:
            entered_char = input("Enter your character: ")
            if len(entered_char) > 1:
                print("Enter only one character per try!")
            elif not entered_char.isalpha():
                print("Enter a character from the latin alphabet!")
            else:
                tries += 1
                if entered_char in secret_word:
                    pos = find_position(secret_word, entered_char)
                    dic = make_dictionary(entered_char, pos)
                    printing(dic, hidden_word)
                else:
                    if lives > 0:
                        print("NO, you got", lives, "lives left")
                        lives = lives - 1
                    else:
                        print("You lost!")
                        break
        else:
            print("You guessed the word!")
            print("You did it in ", tries, " tries!")
            break
