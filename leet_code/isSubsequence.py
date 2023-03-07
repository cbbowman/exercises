def isSubsequence(s: str, t: str) -> bool:
    if len(s) == 0:
        return True
    list_s = list(s)
    list_t = list(t)
    list_new = []
    i = 0

    for c in list_t:
        if c == list_s[i]:
            list_new.append(c)
            i += 1

            if len(s) == i:
                return list_new == list_s

    return list_new == list_s


s = "ab"
t = "baab"

print(isSubsequence(s, t))
