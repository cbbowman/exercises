import string

def is_perm1(str1, str2):

    if len(str1) != len(str2):
        return False

    return sorted(str1) == sorted(str2)

test1 = is_perm1("stop", "pots")==True
test2 = is_perm1("stop", "stoop")==False
test3 = is_perm1("stop", "taps")==False
test4 = is_perm1("", "")==True
if test1 & test2 & test3 & test4:
    print("is_perm1 passed")
else:
    print("is_perm1 failed")

def is_perm2(str1, str2, char_set = 128):
    
    if len(str1) != len(str2):
        return False

    letters = [0] * char_set

    for i in range(len(str1)):
        letters[ord(str1[i])] += 1

    for i in range(len(str2)):
        letters[ord(str2[i])] -= 1
        if letters[ord(str2[i])] < 0:
            return False

    return True

test1 = is_perm2("stop", "pots")==True
test2 = is_perm2("stop", "stoop")==False
test3 = is_perm2("stop", "taps")==False
test4 = is_perm2("", "")==True
if test1 & test2 & test3 & test4:
    print("is_perm2 passed")
else:
    print("is_perm2 failed")
