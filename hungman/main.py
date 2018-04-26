s = 'gaming'
char = "g"

sm = ['*' for i in s]


def findPosition(word, char):
    return [pos for pos, i in enumerate(word) if i == char]


p = findPosition(s, char)


def makeDictionary(char, lst):
    d = {}
    d[char] = lst
    return d


d = makeDictionary(char, p)


def printing(dic, mword):
    for k in dic:
        for v in dic[k]:
            mword[v] = k
    return mword

sd = {"a": [1]}


def merge(dic1, dic2):
    return {**dic1, **dic2}


asd = merge(d, sd)
#print(printing(asd, sm))

lives = 5
while lives >= 0:
    print("Your word is: ", sm)
    if '*' in sm:
        prompt = input("Choose your character ")
        if prompt in s:
            pos = findPosition(s, prompt)
            dic = makeDictionary(prompt, pos)
            printing(dic, sm)
        else:
            if lives > 0:
                print("NO, you got", lives, "lives left")
                lives = lives - 1
            else:
                print("You lost!")
                break
    else:
        print("You guessed the word!")
        break
