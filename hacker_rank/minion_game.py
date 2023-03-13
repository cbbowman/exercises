
def minion_game(string):
    vowels = ["A", "E", "I", "O", "U"]
    consonant = []
    vowel = []
    split = string.split()
    len_s = len(split)

    if len_s == 0:
        return "Draw"

    if len_s == 1:
        if string[0] in vowels:
            return "Kevin 1"
        else:
            return "Stuart 1"


    return score
