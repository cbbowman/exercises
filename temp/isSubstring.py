def isSubsequence(s: str, t: str) -> bool:
    len_t = len(t)
    len_s = len(s)

    if len_s > len_t:
        return False

    if len_s == len_t:
        return s == t

    if len_s == 0:
        return True

    if len_t == 0:
        if len_s == 0:
            return True

        return False

    list_s = list(s)
    list_t = list(t)

    for i, c in enumerate(list_t):
        j = i + len_s

        if list_s == list_t[i:j]:
            return True

        if i == len_t - len_s:
            return False

    return False


s = "dog"
t = "dogabigdgeeedog"

print(isSubsequence(s, t))
