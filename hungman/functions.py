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
            prompt = input("Choose your character ")
            if len(prompt) > 1:
                print("Prompt only one character per try!")
            elif not prompt.isalpha():
                print("Prompt a character from the latin alphabet!")
            else:
                tries += 1
                if prompt in secret_word:
                    pos = find_position(secret_word, prompt)
                    dic = make_dictionary(prompt, pos)
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
            print("You did it in ", tries, " tries")
            break
